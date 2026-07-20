# 📘 Day 20 – Edge Detection & Morphological Operations

## 🗂️ Folder Structure

```
Day-20/
├── edge_detection/
│   └── edge_detection.ipynb              # Sobel + Laplacian + Canny
├── morphological_operations/
│   └── morphological_ops.ipynb           # All 7 morphological ops
├── document_boundary_tool/
│   └── document_boundary_tool.ipynb      # Full mini project + challenge task
└── README.md
```

---

## 🔍 Edge Detection – Sobel vs Laplacian vs Canny

| Feature | Sobel | Laplacian | Canny |
|---|---|---|---|
| Derivative order | 1st | 2nd | 1st (with extra steps) |
| Direction | X or Y separately | All at once | All at once |
| Noise sensitivity | Medium | High (needs blur) | Low (has built-in blur) |
| Output | Gradient magnitude | Edge magnitude | Binary edge map |
| Edge thickness | Thick | Medium | Thin (non-max suppression) |
| Connected edges | No | No | Yes (hysteresis) |
| Best for | Gradient analysis | Fine detail | General edge detection ✅ |
| Industry use | Feature maps | Texture analysis | Object detection, OCR |

**Winner for documents: Canny** — it produces clean, thin, connected edges which is exactly what contour detection needs.

---

## 🔬 Morphological Operations

| Operation | Formula | Purpose |
|---|---|---|
| **Erosion** | Shrinks white regions | Remove small white noise/protrusions |
| **Dilation** | Expands white regions | Fill small holes, connect broken edges |
| **Opening** | Erosion → Dilation | Remove small noise while preserving shape |
| **Closing** | Dilation → Erosion | Fill small gaps/holes while preserving shape |
| **Gradient** | Dilation − Erosion | Extract object boundary/outline |
| **Top Hat** | Original − Opening | Highlight bright spots smaller than kernel |
| **Black Hat** | Closing − Original | Highlight dark spots smaller than kernel |

---

## 🏆 Best Combination for Document Boundary Detection

```
Grayscale
    ↓
GaussianBlur(5×5)         # Remove noise before edge detection
    ↓
Canny(30, 100)            # Detect document edges
    ↓
MorphClose(5×5, iter=2)   # Close gaps in document boundary
    ↓
MorphOpen(5×5, iter=1)    # Remove small noise
    ↓
Dilate(5×5, iter=1)       # Connect nearby edge segments
    ↓
findContours → largest    # Document = biggest closed region
    ↓
approxPolyDP              # Simplify to polygon (4 corners = rectangle)
```

This combination outperformed alternatives because:
- Closing before Opening keeps the document boundary intact while removing internal noise
- Dilation connects edge gaps that Canny may have missed
- `approxPolyDP` with epsilon=2% of perimeter gives stable 4-corner detection

---

## 🚧 Challenges in Document Boundary Detection

| Challenge | Solution |
|---|---|
| Shadow on document edges | Adaptive thresholding or CLAHE pre-processing |
| Curved/bent documents | Increase morph kernel size; use perspective transform after detection |
| Document same color as background | Use CLAHE to enhance contrast before Canny |
| Blurry images | Reduce Canny thresholds (more sensitive) |
| Multiple documents in frame | Filter contours by aspect ratio + min area threshold |
| Tilted documents | `approxPolyDP` + `minAreaRect` for rotated bounding box |

---

## 📋 OpenCV Functions Used

| Function | Purpose |
|---|---|
| `cv2.GaussianBlur()` | Noise reduction before edge detection |
| `cv2.Sobel()` | Directional gradient (X or Y) |
| `cv2.Laplacian()` | 2nd derivative edge detection |
| `cv2.Canny()` | Best-in-class edge detection |
| `cv2.erode()` | Morphological erosion |
| `cv2.dilate()` | Morphological dilation |
| `cv2.morphologyEx(MORPH_OPEN)` | Opening |
| `cv2.morphologyEx(MORPH_CLOSE)` | Closing |
| `cv2.morphologyEx(MORPH_GRADIENT)` | Boundary extraction |
| `cv2.morphologyEx(MORPH_TOPHAT)` | Bright region highlight |
| `cv2.morphologyEx(MORPH_BLACKHAT)` | Dark region highlight |
| `cv2.findContours()` | Find all contours in binary image |
| `cv2.approxPolyDP()` | Approximate contour to polygon |
| `cv2.drawContours()` | Draw detected boundary |

---

## 📅 Date
**July 8, 2026**

> *"Understanding these techniques will make it much easier to build robust Computer Vision applications."*
