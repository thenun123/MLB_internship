# ============================================================
#   Day 21 – Shape Detection System
#   Detects: Circle, Square, Rectangle, Triangle,
#            Pentagon, Hexagon, Polygon
# ============================================================

import cv2
import numpy as np
import os

INPUT  = '../input_images'
OUTPUT = '../output_images'
os.makedirs(OUTPUT, exist_ok=True)


# ── Shape Detection Logic ────────────────────────────────────

def detect_shape(cnt):
    """
    Classify a contour into a geometric shape.
    Uses approxPolyDP to count corners + circularity for circles.
    """
    shape = "Unknown"
    peri  = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.03 * peri, True)
    corners = len(approx)

    # Circularity = 4π × Area / Perimeter²
    # Perfect circle → 1.0
    area          = cv2.contourArea(cnt)
    circularity   = (4 * np.pi * area) / (peri ** 2) if peri > 0 else 0

    if circularity > 0.80:
        shape = "Circle"
    elif corners == 3:
        shape = "Triangle"
    elif corners == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        shape = "Square" if 0.90 <= aspect_ratio <= 1.10 else "Rectangle"
    elif corners == 5:
        shape = "Pentagon"
    elif corners == 6:
        shape = "Hexagon"
    elif corners == 8:
        shape = "Octagon"
    else:
        shape = f"Polygon ({corners})"

    return shape, corners, circularity


def get_shape_color(shape):
    """Return a unique BGR color per shape type."""
    colors = {
        "Circle"   : (0,   200, 255),
        "Square"   : (0,   255,   0),
        "Rectangle": (255, 100,   0),
        "Triangle" : (0,    50, 255),
        "Pentagon" : (255,   0, 180),
        "Hexagon"  : (0,   255, 180),
        "Octagon"  : (180, 255,   0),
    }
    return colors.get(shape, (128, 128, 128))


def process_image(img_path, save_name):
    """
    Run the full shape detection pipeline on one image.
    Saves: original, contours, labeled output.
    """
    img = cv2.imread(img_path)
    if img is None:
        print(f"  ❌ Cannot load: {img_path}")
        return

    gray    = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adaptive threshold works well on both light and dark backgrounds
    thresh = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11, 2
    )

    # Morphological cleanup
    kernel  = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    contours, _ = cv2.findContours(
        cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # ── Save original ─────────────────────────────────────────
    cv2.imwrite(os.path.join(OUTPUT, f'{save_name}_1_original.png'), img)

    # ── Contour result ────────────────────────────────────────
    contour_img = img.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
    cv2.imwrite(os.path.join(OUTPUT, f'{save_name}_2_contours.png'), contour_img)

    # ── Shape detection result ────────────────────────────────
    result   = img.copy()
    detected = []
    shape_counts = {}

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 800:     # Skip tiny noise contours
            continue

        shape, corners, circ = detect_shape(cnt)
        color  = get_shape_color(shape)
        peri   = cv2.arcLength(cnt, True)

        # Draw filled contour (transparent)
        overlay = result.copy()
        cv2.drawContours(overlay, [cnt], -1, color, -1)
        cv2.addWeighted(overlay, 0.25, result, 0.75, 0, result)

        # Draw contour border
        cv2.drawContours(result, [cnt], -1, color, 2)

        # Bounding box for label placement
        x, y, w, h = cv2.boundingRect(cnt)
        cx, cy = x + w // 2, y + h // 2

        # Label: shape name
        label = shape
        (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.55, 2)
        lx = max(0, cx - tw // 2)
        ly = max(20, cy)
        cv2.rectangle(result, (lx-4, ly-th-6), (lx+tw+4, ly+4),
                      (255, 255, 255), -1)
        cv2.putText(result, label, (lx, ly),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)

        # Area label below
        area_txt = f'A={int(area)}'
        cv2.putText(result, area_txt, (lx, ly+18),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.38, (60, 60, 60), 1)

        detected.append({
            'shape' : shape,
            'area'  : area,
            'peri'  : peri,
            'corners': corners,
            'circ'  : circ
        })
        shape_counts[shape] = shape_counts.get(shape, 0) + 1

    cv2.imwrite(os.path.join(OUTPUT, f'{save_name}_3_shapes.png'), result)

    # ── Print results ─────────────────────────────────────────
    print(f"\n  📄 {os.path.basename(img_path)}")
    print(f"     Shapes found: {len(detected)}")
    if detected:
        print(f"     {'Shape':<14} {'Area':>9} {'Perimeter':>11} {'Circularity':>13}")
        print(f"     {'-'*50}")
        for d in sorted(detected, key=lambda x: -x['area']):
            print(f"     {d['shape']:<14} {d['area']:>9.0f} {d['peri']:>11.1f} {d['circ']:>13.3f}")
    for shape, count in shape_counts.items():
        print(f"     → {count}× {shape}")

    return detected


# ── Run on all 10 images ─────────────────────────────────────

print("=" * 60)
print("   SHAPE DETECTION SYSTEM – Day 21")
print("=" * 60)

image_files = sorted([
    f for f in os.listdir(INPUT)
    if f.endswith(('.png', '.jpg', '.jpeg'))
])

all_results = {}
for img_file in image_files:
    save_name = os.path.splitext(img_file)[0]
    img_path  = os.path.join(INPUT, img_file)
    result    = process_image(img_path, save_name)
    if result:
        all_results[img_file] = result

# ── Summary ──────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  FINAL SUMMARY")
print("=" * 60)

total_shapes = 0
shape_totals = {}
for img_file, detections in all_results.items():
    total_shapes += len(detections)
    for d in detections:
        shape_totals[d['shape']] = shape_totals.get(d['shape'], 0) + 1

print(f"\n  Total images processed : {len(all_results)}")
print(f"  Total shapes detected  : {total_shapes}")
print(f"\n  Shape breakdown:")
for shape, count in sorted(shape_totals.items(), key=lambda x: -x[1]):
    bar = "█" * count
    print(f"    {shape:<14} : {count:>3}  {bar}")

print(f"\n✅ All outputs saved to output_images/ (3 files per image = {len(all_results)*3} files)")
