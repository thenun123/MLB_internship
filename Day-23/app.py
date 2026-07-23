# ============================================================
#   🎨 Computer Vision Image Processing Studio
#   Day 23 – Gradio App for Hugging Face Spaces
#   Author: Azeem Naseer
# ============================================================

import cv2
import numpy as np
import gradio as gr
from PIL import Image
import spaces


# ── ZeroGPU requirement ─────────────────────────────────────
# This app is CPU-only (OpenCV), but the Space is provisioned with
# ZeroGPU hardware, which requires at least one @spaces.GPU-decorated
# function to be present at startup. This dummy warmup satisfies that
# check and reserves GPU capacity for future GPU-accelerated features
# without affecting any of the CPU processing functions below.
@spaces.GPU
def _gpu_warmup():
    return True

# ── Helper: convert between PIL and numpy ──────────────────
def to_np(img):
    """PIL → numpy BGR"""
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def to_pil(img):
    """numpy BGR → PIL"""
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


# ════════════════════════════════════════════════════════════
#  CORE PROCESSING FUNCTIONS
# ════════════════════════════════════════════════════════════

def apply_grayscale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


def apply_blur(img, strength=15):
    k = max(1, int(strength)) | 1   # must be odd
    return cv2.GaussianBlur(img, (k, k), 0)


def apply_edge_detection(img, low=50, high=150):
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur  = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, low, high)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)


def apply_rotation(img, angle=90):
    h, w = img.shape[:2]
    M    = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
    return cv2.warpAffine(img, M, (w, h))


def apply_flip(img, mode='Horizontal'):
    code = {'Horizontal': 1, 'Vertical': 0, 'Both': -1}[mode]
    return cv2.flip(img, code)


def apply_brightness_contrast(img, brightness=0, contrast=1.0):
    return cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)


def apply_sharpen(img, strength=1.0):
    kernel = np.array([
        [ 0, -1,  0],
        [-1,  5, -1],
        [ 0, -1,  0]
    ], dtype=np.float32)
    kernel = np.eye(3) * (1 - strength) + kernel * strength
    return cv2.filter2D(img, -1, kernel)


def apply_threshold(img, thresh_val=127, mode='Binary'):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    modes = {
        'Binary'     : cv2.THRESH_BINARY,
        'Binary Inv' : cv2.THRESH_BINARY_INV,
        'Otsu'       : cv2.THRESH_BINARY + cv2.THRESH_OTSU,
        'Adaptive'   : None,
    }
    if mode == 'Adaptive':
        out = cv2.adaptiveThreshold(
            cv2.GaussianBlur(gray, (5, 5), 0), 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
        )
    else:
        tv = 0 if mode == 'Otsu' else int(thresh_val)
        _, out = cv2.threshold(gray, tv, 255, modes[mode])
    return cv2.cvtColor(out, cv2.COLOR_GRAY2BGR)


def apply_contour_detection(img):
    gray   = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur   = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thr = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cnts, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    out = img.copy()
    cv2.drawContours(out, cnts, -1, (0, 255, 0), 2)
    for cnt in cnts:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(out, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.putText(out, f'Contours: {len(cnts)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return out


def apply_shape_detection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thr = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    thr = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, k, iterations=2)
    cnts, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    out = img.copy()

    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if area < 800:
            continue
        peri  = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.03 * peri, True)
        corners = len(approx)
        circ = (4 * np.pi * area / peri ** 2) if peri > 0 else 0

        if circ > 0.80:
            shape = "Circle"
            color = (0, 200, 255)
        elif corners == 3:
            shape = "Triangle"
            color = (0, 50, 255)
        elif corners == 4:
            x, y, w, h = cv2.boundingRect(approx)
            shape = "Square" if 0.9 <= w/h <= 1.1 else "Rectangle"
            color = (0, 255, 0)
        elif corners == 5:
            shape, color = "Pentagon", (255, 0, 180)
        elif corners == 6:
            shape, color = "Hexagon", (0, 255, 180)
        else:
            shape, color = f"Poly({corners})", (128, 128, 0)

        cv2.drawContours(out, [cnt], -1, color, 2)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.putText(out, shape, (x, y - 8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)
    return out


def apply_cartoon(img):
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray  = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 300, 300)
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    return cv2.bitwise_and(color, edges_bgr)


def apply_pencil_sketch(img):
    gray       = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv        = cv2.bitwise_not(gray)
    blur       = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch     = cv2.divide(gray, cv2.bitwise_not(blur), scale=256.0)
    return cv2.cvtColor(sketch.astype(np.uint8), cv2.COLOR_GRAY2BGR)


def apply_emboss(img):
    kernel = np.array([
        [-2, -1,  0],
        [-1,  1,  1],
        [ 0,  1,  2]
    ], dtype=np.float32)
    gray   = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    emboss = cv2.filter2D(gray, -1, kernel) + 128
    return cv2.cvtColor(emboss.astype(np.uint8), cv2.COLOR_GRAY2BGR)


def apply_morph(img, op='Dilation', kernel_size=5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thr = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    ops = {
        'Erosion'   : cv2.erode(thr, k),
        'Dilation'  : cv2.dilate(thr, k),
        'Opening'   : cv2.morphologyEx(thr, cv2.MORPH_OPEN,     k),
        'Closing'   : cv2.morphologyEx(thr, cv2.MORPH_CLOSE,    k),
        'Gradient'  : cv2.morphologyEx(thr, cv2.MORPH_GRADIENT, k),
        'Top Hat'   : cv2.morphologyEx(thr, cv2.MORPH_TOPHAT,   k),
        'Black Hat' : cv2.morphologyEx(thr, cv2.MORPH_BLACKHAT, k),
    }
    result = ops.get(op, thr)
    return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)


# ════════════════════════════════════════════════════════════
#  MAIN PROCESSING ROUTER
# ════════════════════════════════════════════════════════════

def process_image(
    pil_img, operation,
    blur_strength, edge_low, edge_high,
    rotation_angle, flip_mode,
    brightness, contrast,
    sharpen_strength,
    thresh_value, thresh_mode,
    morph_op, morph_kernel
):
    if pil_img is None:
        return None, "⚠️ Please upload an image first."

    img = to_np(pil_img)
    info_lines = []

    if operation == "🖤 Grayscale":
        out = apply_grayscale(img)
        info_lines = ["✅ Converted to grayscale", "Single-channel representation of brightness."]

    elif operation == "🌫️ Gaussian Blur":
        k = max(1, int(blur_strength)) | 1
        out = apply_blur(img, blur_strength)
        info_lines = [f"✅ Gaussian Blur applied", f"Kernel size: {k}×{k}"]

    elif operation == "🔍 Edge Detection (Canny)":
        out = apply_edge_detection(img, edge_low, edge_high)
        info_lines = [f"✅ Canny Edge Detection", f"Thresholds: low={int(edge_low)}, high={int(edge_high)}"]

    elif operation == "🔄 Rotation":
        out = apply_rotation(img, rotation_angle)
        info_lines = [f"✅ Rotated {rotation_angle}°"]

    elif operation == "↔️ Flip":
        out = apply_flip(img, flip_mode)
        info_lines = [f"✅ Flipped: {flip_mode}"]

    elif operation == "☀️ Brightness & Contrast":
        out = apply_brightness_contrast(img, brightness, contrast)
        info_lines = [f"✅ Brightness: {int(brightness):+d}", f"Contrast: {contrast:.1f}×"]

    elif operation == "✏️ Sharpen":
        out = apply_sharpen(img, sharpen_strength)
        info_lines = [f"✅ Sharpened", f"Strength: {sharpen_strength:.1f}"]

    elif operation == "⬛ Threshold":
        out = apply_threshold(img, thresh_value, thresh_mode)
        info_lines = [f"✅ Threshold: {thresh_mode}", f"Value: {int(thresh_value)}"]

    elif operation == "🔷 Contour Detection":
        out = apply_contour_detection(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thr = cv2.threshold(cv2.GaussianBlur(gray, (5,5), 0), 0, 255,
                               cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        cnts, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        info_lines = [f"✅ Contour Detection", f"Contours found: {len(cnts)}"]

    elif operation == "🔶 Shape Detection":
        out = apply_shape_detection(img)
        info_lines = ["✅ Shape Detection", "Labels drawn on each detected shape."]

    elif operation == "🎨 Cartoon Effect":
        out = apply_cartoon(img)
        info_lines = ["✅ Cartoon Effect applied", "Bilateral filter + edge overlay"]

    elif operation == "✏️ Pencil Sketch":
        out = apply_pencil_sketch(img)
        info_lines = ["✅ Pencil Sketch effect", "Grayscale + dodge blend"]

    elif operation == "🌑 Emboss":
        out = apply_emboss(img)
        info_lines = ["✅ Emboss filter applied"]

    elif operation == "🔬 Morphological Operations":
        out = apply_morph(img, morph_op, int(morph_kernel))
        info_lines = [f"✅ Morphology: {morph_op}", f"Kernel: {int(morph_kernel)}×{int(morph_kernel)}"]

    else:
        out = img.copy()
        info_lines = ["⚠️ No operation selected"]

    h, w = img.shape[:2]
    info_lines += [f"Image size: {w}×{h} px"]
    info_text = "\n".join(info_lines)

    return to_pil(out), info_text


# ════════════════════════════════════════════════════════════
#  GRADIO INTERFACE
# ════════════════════════════════════════════════════════════

OPERATIONS = [
    "🖤 Grayscale",
    "🌫️ Gaussian Blur",
    "🔍 Edge Detection (Canny)",
    "🔄 Rotation",
    "↔️ Flip",
    "☀️ Brightness & Contrast",
    "✏️ Sharpen",
    "⬛ Threshold",
    "🔷 Contour Detection",
    "🔶 Shape Detection",
    "🎨 Cartoon Effect",
    "✏️ Pencil Sketch",
    "🌑 Emboss",
    "🔬 Morphological Operations",
]

with gr.Blocks(
    title="CV Image Processing Studio",
    theme=gr.themes.Soft(primary_hue="blue"),
) as demo:

    gr.Markdown("""
    # 🎨 Computer Vision Image Processing Studio
    **Day 23 – MLB Internship Bootcamp | Azeem Naseer**

    Upload any image and apply 14 different Computer Vision operations.
    Adjust the parameters using the sliders and dropdowns, then click **Process Image**.
    """)

    with gr.Row():

        # ── Left column: input ────────────────────────────────
        with gr.Column(scale=1):
            input_img = gr.Image(
                label="📤 Upload Image",
                type="pil",
                height=320
            )
            operation = gr.Dropdown(
                choices=OPERATIONS,
                value="🖤 Grayscale",
                label="🔧 Select Operation"
            )

            gr.Markdown("### ⚙️ Operation Parameters")

            with gr.Accordion("🌫️ Blur Settings", open=False):
                blur_strength = gr.Slider(1, 51, value=15, step=2, label="Blur Strength (kernel size)")

            with gr.Accordion("🔍 Edge Detection Settings", open=False):
                edge_low  = gr.Slider(0, 255, value=50,  label="Canny Low Threshold")
                edge_high = gr.Slider(0, 255, value=150, label="Canny High Threshold")

            with gr.Accordion("🔄 Rotation Settings", open=False):
                rotation_angle = gr.Slider(-180, 180, value=90, step=1, label="Rotation Angle (°)")

            with gr.Accordion("↔️ Flip Settings", open=False):
                flip_mode = gr.Radio(
                    ["Horizontal", "Vertical", "Both"],
                    value="Horizontal", label="Flip Direction"
                )

            with gr.Accordion("☀️ Brightness & Contrast", open=False):
                brightness = gr.Slider(-100, 100, value=0,   step=1,   label="Brightness")
                contrast   = gr.Slider(0.1,  3.0, value=1.0, step=0.1, label="Contrast")

            with gr.Accordion("✏️ Sharpen Settings", open=False):
                sharpen_strength = gr.Slider(0.0, 3.0, value=1.0, step=0.1, label="Sharpen Strength")

            with gr.Accordion("⬛ Threshold Settings", open=False):
                thresh_value = gr.Slider(0, 255, value=127, step=1, label="Threshold Value")
                thresh_mode  = gr.Radio(
                    ["Binary", "Binary Inv", "Otsu", "Adaptive"],
                    value="Binary", label="Threshold Mode"
                )

            with gr.Accordion("🔬 Morphological Settings", open=False):
                morph_op     = gr.Dropdown(
                    ["Erosion", "Dilation", "Opening", "Closing",
                     "Gradient", "Top Hat", "Black Hat"],
                    value="Dilation", label="Morphological Operation"
                )
                morph_kernel = gr.Slider(3, 21, value=5, step=2, label="Kernel Size")

            process_btn = gr.Button("🚀 Process Image", variant="primary", size="lg")

        # ── Right column: output ──────────────────────────────
        with gr.Column(scale=1):
            output_img  = gr.Image(label="🖼️ Processed Image", type="pil", height=320)
            info_box    = gr.Textbox(label="ℹ️ Info", lines=4, interactive=False)

            gr.Markdown("### 📥 Download Result")
            output_file = gr.Image(
                label="Right-click → Save image as...",
                type="pil",
                interactive=False
            )

    # ── Footer ────────────────────────────────────────────────
    gr.Markdown("""
    ---
    **Operations available:** Grayscale • Gaussian Blur • Canny Edge Detection •
    Rotation • Flip • Brightness & Contrast • Sharpen • Threshold •
    Contour Detection • Shape Detection • Cartoon Effect • Pencil Sketch •
    Emboss • Morphological Operations

    > Built with OpenCV + Gradio | MLB Internship Bootcamp 2026
    """)

    # ── Event handler ─────────────────────────────────────────
    def on_process(
        pil_img, operation,
        blur_strength, edge_low, edge_high,
        rotation_angle, flip_mode,
        brightness, contrast,
        sharpen_strength,
        thresh_value, thresh_mode,
        morph_op, morph_kernel
    ):
        result, info = process_image(
            pil_img, operation,
            blur_strength, edge_low, edge_high,
            rotation_angle, flip_mode,
            brightness, contrast,
            sharpen_strength,
            thresh_value, thresh_mode,
            morph_op, morph_kernel
        )
        return result, info, result   # output + info + download copy

    process_btn.click(
        fn=on_process,
        inputs=[
            input_img, operation,
            blur_strength, edge_low, edge_high,
            rotation_angle, flip_mode,
            brightness, contrast,
            sharpen_strength,
            thresh_value, thresh_mode,
            morph_op, morph_kernel
        ],
        outputs=[output_img, info_box, output_file]
    )


# ── Launch ───────────────────────────────────────────────────
if __name__ == "__main__":
    demo.launch()
