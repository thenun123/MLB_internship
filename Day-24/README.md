---
title: OCR Document Reader
emoji: 🔍
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: "4.44.0"
app_file: app.py
pinned: false
license: mit
---

# 🔍 OCR Document Reader

**Day 24 – MLB Internship Bootcamp | Azeem Naseer**

Extract text from any image using EasyOCR with preprocessing options and downloadable results.

---

## 🚀 Links

- **GitHub:** https://github.com/thenun123/MLB_internship
- **Hugging Face Space:** *(add link after deployment)*

---

## 🗂️ Folder Structure

```
Day-24/
├── app.py                    # Gradio app (main entry point)
├── requirements.txt          # Dependencies
├── README.md                 # This file
├── ocr_practice/
│   └── ocr_practice.py       # Practice script testing all 10 images
├── sample_images/            # 10 synthetic text images
│   ├── img01_document.png
│   ├── img02_receipt.png
│   ├── img03_signboard.png
│   ├── img04_book_page.png
│   ├── img05_handwritten.png
│   ├── img06_id_card.png
│   ├── img07_low_light.png
│   ├── img08_tilted.png
│   ├── img09_number_plate.png
│   └── img10_multicolumn.png
└── extracted_texts/          # OCR output: .txt + annotated images
```

---

## 🤔 What is OCR?

**Optical Character Recognition (OCR)** is a technology that converts images containing text into machine-readable text. It works by:

1. **Preprocessing** the image (denoise, binarize, enhance contrast)
2. **Detecting** text regions using deep learning models
3. **Recognizing** characters within each region
4. **Assembling** characters into words and lines

**Real-world applications:**
- Document digitization and archiving
- Invoice and receipt processing
- ID card and passport reading
- Number plate recognition
- Book and form scanning

---

## 📚 OCR Library Comparison

| Feature | Tesseract | EasyOCR | PaddleOCR |
|---|---|---|---|
| Language support | 100+ | 80+ | 80+ |
| Accuracy | Good | **Very Good** | Excellent |
| Speed | Fast | Medium | Fast |
| GPU support | No | Yes | Yes |
| Multi-threading | ✅ Yes | ✅ Yes | ✅ Yes |
| Handwriting | Poor | Fair | Good |
| Setup difficulty | Medium | Easy | Medium |
| Best for | Basic text | General use | Production |

### 🔀 Which OCR Libraries Support Multi-threading?

| Library | Multi-threading | Details |
|---|---|---|
| **Tesseract** | ✅ Yes | Uses OpenMP; set `OMP_THREAD_LIMIT` env var |
| **EasyOCR** | ✅ Yes | PyTorch DataLoader with `num_workers` param |
| **PaddleOCR** | ✅ Yes | Built-in CPU/GPU multi-threading via PaddlePaddle |

**Why EasyOCR was chosen:**
- Easiest setup (`pip install easyocr`)
- No system-level Tesseract binary needed
- Strong accuracy on printed text
- Returns bounding boxes + confidence scores natively
- Works well in Hugging Face Spaces (no extra system deps)

---

## 🔧 Preprocessing Techniques & Results

| Mode | Best For | Accuracy Improvement |
|---|---|---|
| None | Clean printed text | Baseline |
| Grayscale Only | Color images | +5–10% |
| CLAHE | Low-light, faded docs | +15–25% |
| Gaussian + Threshold | Noisy backgrounds | +10–20% |
| **Full Pipeline** | Most documents ✅ | +20–30% |
| Sharpen | Blurry images | +10–15% |
| Denoise | Scanned/grainy images | +10–20% |

---

## 📊 OCR Practice Results (10 Images)

| Image | Type | Blocks Found | Avg Confidence | Notes |
|---|---|---|---|---|
| img01_document | Invoice | 6 | 0.90 | Clean, high accuracy |
| img02_receipt | Receipt | 17 | 0.94 | Best result |
| img03_signboard | Sign | 3 | 0.58 | White-on-dark needs tuning |
| img04_book_page | Book text | 8 | 0.87 | Good paragraph detection |
| img05_handwritten | Handwritten | 11 | 0.13 | Hardest case for OCR |
| img06_id_card | ID Card | 5 | 0.45 | Small text challenge |
| img07_low_light | Dark doc | 6 | 0.48 | CLAHE helps significantly |
| img08_tilted | Rotated | 13 | 0.97 | EasyOCR handles tilt well |
| img09_number_plate | Plate | 1 | 0.84 | Partial detection |
| img10_multicolumn | Multi-col | 17 | 0.91 | Columns detected separately |

---

## 🚧 Challenges Faced

| Challenge | Solution |
|---|---|
| Handwritten text low accuracy | EasyOCR is not optimized for cursive; needs fine-tuned model |
| White text on dark background | Invert image before preprocessing |
| Tilted/rotated documents | EasyOCR auto-detects rotation; deskewing helps further |
| Low contrast images | CLAHE preprocessing significantly improves results |
| Small text | Upscale image 2× before OCR |
| Multi-column layouts | Columns detected separately; merge by X coordinate |

---

## 🏃 How to Run Locally

```bash
pip install -r requirements.txt
python app.py
# Opens at http://localhost:7860
```

---

## 🚀 Deploy to Hugging Face Spaces

1. Go to [huggingface.co](https://huggingface.co) → New Space → **Gradio**
2. Upload: `app.py`, `requirements.txt`, `README.md`
3. Wait ~3 minutes for build
4. App goes live automatically

---

## 📅 Date
**July 11, 2026**

> *"OCR bridges the gap between physical documents and digital data processing."*
