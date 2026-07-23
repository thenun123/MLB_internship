---
title: CV Image Processing Studio
emoji: 🎨
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "4.0.0"
app_file: app.py
pinned: false
license: mit
---

# 🎨 Computer Vision Image Processing Studio

**Day 23 – MLB Internship Bootcamp | Azeem Naseer**

A complete Computer Vision web application built with OpenCV and Gradio, combining all techniques learned over the past week.

---

## 🚀 Live Demo

👉 **Hugging Face Space:** [Add your link here after deployment]
👉 **GitHub Repository:** https://github.com/thenun123/MLB_internship

---

## 🗂️ Folder Structure

```
Day-23/
├── app.py                  # Main Gradio application
├── requirements.txt        # Python dependencies
├── README.md               # This file (also used as HF Space README)
├── sample_images/          # 3 sample input images
│   ├── sample1_shapes.png
│   ├── sample2_landscape.png
│   └── sample3_document.png
└── sample_outputs/         # 8 sample output images
    ├── out1_grayscale.png
    ├── out2_edges.png
    ├── out3_contours.png
    ├── out4_shapes.png
    ├── out5_cartoon.png
    ├── out6_sketch.png
    ├── out7_bright.png
    └── out8_sharp.png
```

---

## 🔧 14 Operations Available

| # | Operation | Description |
|---|---|---|
| 1 | 🖤 Grayscale | Convert image to single-channel brightness |
| 2 | 🌫️ Gaussian Blur | Smooth image to reduce noise |
| 3 | 🔍 Edge Detection (Canny) | Detect edges with adjustable thresholds |
| 4 | 🔄 Rotation | Rotate image by any angle |
| 5 | ↔️ Flip | Flip horizontally, vertically, or both |
| 6 | ☀️ Brightness & Contrast | Adjust image exposure |
| 7 | ✏️ Sharpen | Enhance fine details |
| 8 | ⬛ Threshold | Binary/Otsu/Adaptive thresholding |
| 9 | 🔷 Contour Detection | Find and draw object boundaries |
| 10 | 🔶 Shape Detection | Identify and label geometric shapes |
| 11 | 🎨 Cartoon Effect | Stylize image as cartoon |
| 12 | ✏️ Pencil Sketch | Convert image to pencil drawing |
| 13 | 🌑 Emboss | Apply emboss texture filter |
| 14 | 🔬 Morphological Operations | Erosion, Dilation, Opening, Closing, etc. |

---

## 🏃 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/thenun123/MLB_internship.git
cd MLB_internship/Day-23

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
# → Opens at http://localhost:7860
```

---

## 🚀 Deploy to Hugging Face Spaces

```bash
# 1. Create a new Space on huggingface.co
#    → New Space → SDK: Gradio → Name: cv-studio

# 2. Push this folder
git init
git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/cv-studio
git add .
git commit -m "Day 23: CV Image Processing Studio"
git push origin main
```

---

## 🧠 Concepts Applied

| Concept | Day Learned |
|---|---|
| Image reading, properties, BGR/RGB | Day 18 |
| Resize, Crop, Rotate, Flip | Day 18 |
| Drawing shapes & text | Day 18 |
| Brightness & Contrast, Blur | Day 19 |
| Edge Detection (Canny, Sobel, Laplacian) | Day 20 |
| Morphological Operations | Day 20 |
| Contour Detection | Day 21 |
| Shape Detection | Day 21 |
| Gradio UI + Deployment | Day 23 |

---

## 📅 Date
**July 11, 2026**

> *"Build it. Ship it. Share it."*
