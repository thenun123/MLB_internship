# ============================================================
#   Day 24 – OCR Practice with EasyOCR
#   Tests OCR on 10 different image types with preprocessing
# ============================================================

import easyocr
import cv2
import numpy as np
import os

INPUT  = '../sample_images'
OUTPUT = '../extracted_texts'
os.makedirs(OUTPUT, exist_ok=True)

print("=" * 60)
print("  OCR PRACTICE – EasyOCR")
print("=" * 60)
print("\n📦 Loading EasyOCR model (English)...")

reader = easyocr.Reader(['en'], gpu=False, verbose=False)
print("✅ EasyOCR ready!\n")


# ── Preprocessing pipeline ───────────────────────────────────

def preprocess(img):
    """Apply preprocessing to improve OCR accuracy."""
    # 1. Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 2. CLAHE for contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    # 3. Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(enhanced, (3,3), 0)
    # 4. Adaptive threshold for binarization
    binary = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )
    return binary


def run_ocr(img_path, use_preprocessing=False):
    """Run EasyOCR on an image, with or without preprocessing."""
    img = cv2.imread(img_path)
    if img is None:
        return [], img

    if use_preprocessing:
        processed = preprocess(img)
        results   = reader.readtext(processed)
    else:
        results   = reader.readtext(img)

    return results, img


def draw_ocr_results(img, results):
    """Draw bounding boxes and text on the image."""
    out = img.copy()
    for (bbox, text, conf) in results:
        pts = np.array(bbox, np.int32).reshape((-1, 1, 2))
        cv2.polylines(out, [pts], True, (0, 255, 0), 2)
        x, y = int(bbox[0][0]), int(bbox[0][1])
        cv2.putText(out, f"{text} ({conf:.2f})",
                    (x, max(y-5, 15)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1)
    return out


def save_text(filename, results, img_name, preprocessed=False):
    """Save extracted text to a .txt file."""
    lines = [
        f"OCR Results – {img_name}",
        f"Preprocessing: {'Yes' if preprocessed else 'No'}",
        "=" * 50,
        ""
    ]
    for i, (bbox, text, conf) in enumerate(results, 1):
        lines.append(f"[{i}] Text: {text:<30} Confidence: {conf:.3f}")
    lines.append("")
    lines.append(f"Total text blocks found: {len(results)}")

    full_text = "\n".join(lines)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_text)
    return full_text


# ── Process all 10 images ────────────────────────────────────

images = sorted([
    f for f in os.listdir(INPUT)
    if f.endswith(('.png','.jpg','.jpeg'))
])

all_results = {}

for img_file in images:
    img_path = os.path.join(INPUT, img_file)
    name     = os.path.splitext(img_file)[0]

    print(f"\n{'─'*55}")
    print(f"  📄 {img_file}")
    print(f"{'─'*55}")

    # Raw OCR
    results_raw, img = run_ocr(img_path, use_preprocessing=False)
    # Preprocessed OCR
    results_pre, _   = run_ocr(img_path, use_preprocessing=True)

    # Pick better result (more text or higher avg confidence)
    def avg_conf(r): return np.mean([c for _,_,c in r]) if r else 0
    best = results_pre if (len(results_pre) >= len(results_raw) and
                           avg_conf(results_pre) >= avg_conf(results_raw)) \
           else results_raw
    used_pre = best is results_pre

    # Print results
    print(f"  Raw OCR    : {len(results_raw)} blocks | avg conf: {avg_conf(results_raw):.3f}")
    print(f"  Preprocessed: {len(results_pre)} blocks | avg conf: {avg_conf(results_pre):.3f}")
    print(f"  Using      : {'Preprocessed ✅' if used_pre else 'Raw ✅'}")
    print(f"\n  Extracted text:")
    for bbox, text, conf in best:
        print(f"    [{conf:.2f}] {text}")

    # Save text file
    txt_path = os.path.join(OUTPUT, f"{name}_extracted.txt")
    save_text(txt_path, best, img_file, used_pre)

    # Save annotated image
    annotated = draw_ocr_results(img, best)
    cv2.imwrite(os.path.join(OUTPUT, f"{name}_annotated.png"), annotated)

    all_results[img_file] = {
        'raw'     : results_raw,
        'pre'     : results_pre,
        'best'    : best,
        'used_pre': used_pre
    }


# ── Summary ──────────────────────────────────────────────────
print(f"\n{'='*60}")
print("  PRACTICE SUMMARY")
print(f"{'='*60}")
print(f"\n  {'Image':<35} {'Blocks':>7} {'Avg Conf':>10} {'Preproc':>9}")
print(f"  {'─'*63}")
for img_file, data in all_results.items():
    b    = data['best']
    conf = np.mean([c for _,_,c in b]) if b else 0
    pre  = '✅' if data['used_pre'] else '❌'
    print(f"  {img_file:<35} {len(b):>7} {conf:>10.3f} {pre:>9}")

print(f"\n✅ Text files saved to extracted_texts/")
print(f"✅ Annotated images saved to extracted_texts/")
