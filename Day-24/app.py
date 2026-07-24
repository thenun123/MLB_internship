# ============================================================
#   🔍 OCR Document Reader – Day 24
#   EasyOCR + Gradio for Hugging Face Spaces
#   Compatible with Gradio 4.x / 5.x / 6.x
#   Author: Azeem Naseer
# ============================================================

import spaces
import easyocr
import cv2
import numpy as np
import gradio as gr
from PIL import Image
import os
import tempfile

# ── Load EasyOCR reader (cached) ─────────────────────────────
READER = None

def get_reader(lang='en'):
    global READER
    if READER is None:
        READER = easyocr.Reader(['en'], gpu=True, verbose=False)
    return READER


# ── Preprocessing functions ───────────────────────────────────

def preprocess_image(img_np, mode='None'):
    """Apply selected preprocessing to a BGR numpy image."""
    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    if mode == 'None':
        return img_np

    elif mode == 'Grayscale Only':
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    elif mode == 'CLAHE (Contrast Enhance)':
        clahe    = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        enhanced = clahe.apply(gray)
        return cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)

    elif mode == 'Gaussian Blur + Threshold':
        blurred = cv2.GaussianBlur(gray, (3,3), 0)
        binary  = cv2.adaptiveThreshold(
            blurred, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2
        )
        return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

    elif mode == 'Full Pipeline (Best)':
        clahe    = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        enhanced = clahe.apply(gray)
        blurred  = cv2.GaussianBlur(enhanced, (3,3), 0)
        binary   = cv2.adaptiveThreshold(
            blurred, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2
        )
        return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

    elif mode == 'Sharpen':
        kernel   = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], np.float32)
        sharpened = cv2.filter2D(gray, -1, kernel)
        return cv2.cvtColor(sharpened, cv2.COLOR_GRAY2BGR)

    elif mode == 'Denoise':
        denoised = cv2.fastNlMeansDenoising(gray, h=10)
        return cv2.cvtColor(denoised, cv2.COLOR_GRAY2BGR)

    return img_np


def draw_boxes(img_np, results):
    """Draw green bounding boxes and red text labels."""
    out = img_np.copy()
    for (bbox, text, conf) in results:
        pts = np.array(bbox, np.int32).reshape((-1,1,2))
        cv2.polylines(out, [pts], True, (0,200,0), 2)
        x, y = int(bbox[0][0]), max(int(bbox[0][1]) - 6, 14)
        label = f"{text} [{conf:.0%}]"
        (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.45, 1)
        cv2.rectangle(out, (x, y-th-4), (x+tw+4, y+4), (0,0,0), -1)
        cv2.putText(out, label, (x+2, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0,255,0), 1)
    return out


# ── Main OCR function ─────────────────────────────────────────

@spaces.GPU
def run_ocr(pil_img, preprocess_mode, min_confidence, paragraph_mode):
    """
    Main OCR pipeline called by Gradio.
    Returns: annotated image, plain text, stats, txt file path
    """
    if pil_img is None:
        return None, "⚠️ Please upload an image.", "", None

    # PIL → numpy BGR
    img_np = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    # Preprocessing
    processed_np = preprocess_image(img_np, preprocess_mode)
    processed_rgb = cv2.cvtColor(processed_np, cv2.COLOR_BGR2RGB)

    # OCR
    reader  = get_reader()
    results = reader.readtext(processed_np, paragraph=paragraph_mode)

    # Filter by confidence
    min_conf = min_confidence / 100.0
    filtered = [(bbox, text, conf) for bbox, text, conf in results
                if conf >= min_conf]

    # Annotated image
    annotated_np  = draw_boxes(img_np, filtered)
    annotated_pil = Image.fromarray(cv2.cvtColor(annotated_np, cv2.COLOR_BGR2RGB))

    # Build plain text output
    if filtered:
        lines = [text for _, text, _ in filtered]
        plain_text = "\n".join(lines)
    else:
        plain_text = "(No text detected above confidence threshold)"

    # Stats
    if filtered:
        confs     = [c for _,_,c in filtered]
        avg_conf  = np.mean(confs)
        stats_str = (
            f"✅ Text blocks found : {len(filtered)}\n"
            f"📊 Average confidence: {avg_conf:.1%}\n"
            f"🔝 Highest confidence: {max(confs):.1%}\n"
            f"🔻 Lowest confidence : {min(confs):.1%}\n"
            f"🔧 Preprocessing     : {preprocess_mode}"
        )
    else:
        stats_str = "⚠️ No text detected. Try a different preprocessing mode."

    # Save .txt file
    tmp = tempfile.NamedTemporaryFile(
        delete=False, suffix='.txt', mode='w', encoding='utf-8'
    )
    tmp.write(f"OCR Extracted Text\n{'='*40}\n\n")
    for i, (bbox, text, conf) in enumerate(filtered, 1):
        tmp.write(f"[Block {i}] Confidence: {conf:.1%}\n{text}\n\n")
    tmp.write(f"\n{'='*40}\nTotal blocks: {len(filtered)}\n")
    tmp.write(f"Preprocessing: {preprocess_mode}\n")
    tmp.close()

    return annotated_pil, plain_text, stats_str, tmp.name


# ════════════════════════════════════════════════════════════
#  GRADIO INTERFACE  (Gradio 4+ compatible)
# ════════════════════════════════════════════════════════════

PREPROCESS_OPTIONS = [
    "None",
    "Grayscale Only",
    "CLAHE (Contrast Enhance)",
    "Gaussian Blur + Threshold",
    "Full Pipeline (Best)",
    "Sharpen",
    "Denoise",
]

with gr.Blocks(
    title="OCR Document Reader",
    theme=gr.themes.Soft(primary_hue="indigo"),
) as demo:

    gr.Markdown("""
    # 🔍 OCR Document Reader
    **Day 24 – MLB Internship Bootcamp | Azeem Naseer**

    Upload any image containing text. The app will extract all readable text using **EasyOCR**,
    draw bounding boxes around detected words, and let you download the result as a `.txt` file.
    """)

    with gr.Row():

        # ── Left: Input ───────────────────────────────────────
        with gr.Column(scale=1):
            input_image = gr.Image(
                label="📤 Upload Image",
                type="pil",
                height=320
            )

            gr.Markdown("### ⚙️ OCR Settings")

            preprocess_mode = gr.Dropdown(
                choices=PREPROCESS_OPTIONS,
                value="Full Pipeline (Best)",
                label="🔧 Preprocessing Mode",
                info="Full Pipeline gives best results for most images"
            )

            min_confidence = gr.Slider(
                minimum=0, maximum=100, value=30, step=5,
                label="Minimum Confidence (%)",
                info="Filter out low-confidence detections"
            )

            paragraph_mode = gr.Checkbox(
                value=False,
                label="Paragraph Mode",
                info="Merge nearby text into paragraphs"
            )

            ocr_btn = gr.Button(
                "🚀 Extract Text",
                variant="primary",
                size="lg"
            )

            gr.Markdown("""
            **💡 Tips:**
            - Use **Full Pipeline** for scanned/printed documents
            - Use **CLAHE** for low-light or faded images
            - Use **Denoise** for noisy/grainy images
            - Lower confidence = more text but may include noise
            """)

        # ── Right: Output ─────────────────────────────────────
        with gr.Column(scale=1):
            annotated_img = gr.Image(
                label="🖼️ Detected Text (with bounding boxes)",
                type="pil",
                height=320
            )
            extracted_text = gr.Textbox(
                label="📝 Extracted Text",
                lines=8,
                show_copy_button=True,
                placeholder="Extracted text will appear here..."
            )
            stats_box = gr.Textbox(
                label="📊 Statistics",
                lines=5,
                interactive=False
            )
            download_file = gr.File(
                label="📥 Download Extracted Text (.txt)"
            )

    # ── Examples ─────────────────────────────────────────────
    gr.Markdown("---")
    gr.Markdown("### 📂 Try Sample Images")
    gr.Markdown("*(Upload your own image or use the samples above)*")

    # ── How it works ─────────────────────────────────────────
    with gr.Accordion("ℹ️ How It Works", open=False):
        gr.Markdown("""
        **Pipeline:**
        1. Upload image
        2. Preprocessing (grayscale, CLAHE, blur, threshold)
        3. EasyOCR detects text regions with bounding boxes
        4. Confidence filtering removes low-quality detections
        5. Results displayed + saved as `.txt` file

        **Preprocessing Modes:**
        | Mode | Best For |
        |---|---|
        | None | High-quality printed text |
        | Grayscale | Color images with clear text |
        | CLAHE | Low-light, faded documents |
        | Gaussian + Threshold | Noisy backgrounds |
        | Full Pipeline | Most document types ✅ |
        | Sharpen | Blurry images |
        | Denoise | Scanned noisy documents |
        """)

    gr.Markdown("""
    ---
    > Built with **EasyOCR** + **Gradio** | MLB Internship Bootcamp 2026 | Azeem Naseer
    """)

    # ── Wire up ───────────────────────────────────────────────
    ocr_btn.click(
        fn=run_ocr,
        inputs=[input_image, preprocess_mode, min_confidence, paragraph_mode],
        outputs=[annotated_img, extracted_text, stats_box, download_file]
    )

    # Also trigger on image upload
    input_image.upload(
        fn=run_ocr,
        inputs=[input_image, preprocess_mode, min_confidence, paragraph_mode],
        outputs=[annotated_img, extracted_text, stats_box, download_file]
    )


if __name__ == "__main__":
    demo.launch()