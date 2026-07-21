# 📘 Day 21 – Contours & Shape Detection

## 🗂️ Folder Structure

```
Day-21/
├── scripts/
│   ├── 01_contour_detection.py     # Contour practice: find, draw, measure
│   └── 02_shape_detection.py       # Shape Detection System (mini project + challenge)
├── input_images/                   # 10 synthetic shape images
│   ├── img01_basic_shapes.png
│   ├── img02_triangles.png
│   ├── img03_mixed_shapes.png
│   ├── img04_polygons.png
│   ├── img05_circles.png
│   ├── img06_rectangles.png
│   ├── img07_dark_bg.png
│   ├── img08_size_variation.png
│   ├── img09_polygons_variety.png
│   └── img10_complex_scene.png
├── output_images/                  # 3 output files per image = 30 files
│   ├── img01_..._1_original.png
│   ├── img01_..._2_contours.png
│   ├── img01_..._3_shapes.png
│   └── ... (30 files total)
└── README.md
```

---

## 🔍 What are Contours?

Contours are **curves that join all continuous points along a boundary that have the same color or intensity**. In OpenCV, contours are detected from binary (black & white) images where the object boundaries appear as white regions on a black background.

**Key use cases:**
- Object detection and counting
- Shape analysis and recognition
- Motion detection
- Document boundary detection
- Measuring object dimensions

---

## ⚙️ How Contour Detection Works

```
Original Image
    ↓
Grayscale Conversion  (cv2.cvtColor)
    ↓
Gaussian Blur         (cv2.GaussianBlur) — reduce noise
    ↓
Thresholding          (cv2.threshold or cv2.adaptiveThreshold)
    ↓
Find Contours         (cv2.findContours)
    ↓
Analyze / Draw        (cv2.drawContours, boundingRect, etc.)
```

---

## 🔷 Shapes Detected

| Shape | Detection Method | Key Property |
|---|---|---|
| **Circle** | Circularity > 0.80 | `4π×Area / Perimeter²` close to 1.0 |
| **Square** | 4 corners + aspect ratio 0.9–1.1 | `approxPolyDP` returns 4 points |
| **Rectangle** | 4 corners + any aspect ratio | `approxPolyDP` returns 4 points |
| **Triangle** | 3 corners | `approxPolyDP` returns 3 points |
| **Pentagon** | 5 corners | `approxPolyDP` returns 5 points |
| **Hexagon** | 6 corners | `approxPolyDP` returns 6 points |
| **Octagon** | 8 corners | `approxPolyDP` returns 8 points |
| **Polygon** | Any other | Returns corner count |

---

## 📐 Key OpenCV Functions Used

| Function | Purpose |
|---|---|
| `cv2.findContours(img, mode, method)` | Find all contours in binary image |
| `cv2.drawContours(img, contours, idx, color, thickness)` | Draw contours |
| `cv2.contourArea(cnt)` | Area enclosed by contour (pixels²) |
| `cv2.arcLength(cnt, closed)` | Perimeter of contour |
| `cv2.approxPolyDP(cnt, epsilon, closed)` | Approximate contour to polygon |
| `cv2.boundingRect(cnt)` | Axis-aligned bounding rectangle (x,y,w,h) |
| `cv2.minEnclosingCircle(cnt)` | Smallest circle enclosing the contour |
| `cv2.adaptiveThreshold()` | Threshold that adapts to local brightness |

---

## 📊 Results Summary

| Image | Shapes Detected |
|---|---|
| img01_basic_shapes | Circle, Rectangle, Square |
| img02_triangles | Triangle × 2 |
| img03_mixed_shapes | Circle × 2, Square × 2, Triangle |
| img04_polygons | Hexagon, Pentagon |
| img05_circles | Circle × 3, Octagon × 2 |
| img06_rectangles | Rectangle × 5, Square |
| img07_dark_bg | Circle × 3, Hexagon |
| img08_size_variation | Circle × 2, Rectangle × 2, Octagon |
| img09_polygons_variety | Circle × 2, Pentagon, Triangle, Square |
| img10_complex_scene | Circle × 2, Triangle, Rectangle, Square, Hexagon |
| **Total** | **42 shapes across 10 images** |

---

## 🚧 Challenges Faced

| Challenge | Solution |
|---|---|
| Noisy edges causing too many small contours | Added minimum area filter (`area < 800` = skip) |
| Circles detected as polygons | Added circularity check `4π×A/P²` before corner count |
| Shapes merging on touching boundaries | Used `RETR_EXTERNAL` to get only outermost contours |
| Dark background images threshold inverted | Used `THRESH_BINARY_INV` + `adaptiveThreshold` |
| Label placement overlapping shapes | Computed centroid from bounding box center |

---

## 📅 Date
**July 9, 2026**

> *"Contours are the foundation of object detection and image segmentation — understanding them makes everything else easier."*
