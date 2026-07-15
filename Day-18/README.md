# 📘 Day 18 – OpenCV Fundamentals & Basic Image Processing

## 🗂️ Folder Structure

```
Day-18/
├── opencv_practice/
│   └── opencv_fundamentals.py          # All 7 practice programs in one Colab notebook
├── image_processing_toolkit/
│   └── image_toolkit.py                # Menu-driven toolkit (12 operations)
├── challenge_task/
│   └── challenge_5_images.py           # All ops on 5 images (landscape/person/vehicle/doc/object)
└── README.md
```

---

## 🎨 BGR vs RGB

OpenCV reads images in **BGR** (Blue-Green-Red) order by default — the opposite of the standard RGB used by most other tools (matplotlib, PIL, web browsers).

| | Channel Order | Example Use |
|---|---|---|
| **BGR** | Blue → Green → Red | OpenCV default |
| **RGB** | Red → Green → Blue | matplotlib, PIL, web |

If you display a BGR image directly in matplotlib without converting, the red and blue channels are swapped and the image looks wrong. Always use:
```python
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
```

---

## 🖤 Grayscale Images

A **grayscale image** has only **1 channel** instead of 3. Each pixel holds a single intensity value from 0 (black) to 255 (white).

**Why grayscale is used:**
- Reduces computation (1/3 the data of a color image)
- Many CV algorithms don't need color (edge detection, thresholding, face detection)
- Removes irrelevant color variation — focuses on structure and shape
- Used in medical imaging, document scanning, and preprocessing for ML

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Shape changes from (H, W, 3) → (H, W)
```

---

## 🔧 OpenCV Functions Used

| Function | Purpose |
|---|---|
| `cv2.imread(path)` | Load image from disk |
| `cv2.imwrite(path, img)` | Save image to disk |
| `cv2.cvtColor(img, flag)` | Convert color space (BGR↔RGB, BGR→GRAY) |
| `cv2.resize(img, (w, h))` | Resize image |
| `cv2.flip(img, code)` | Flip: 0=vertical, 1=horizontal, -1=both |
| `cv2.getRotationMatrix2D(center, angle, scale)` | Create rotation matrix |
| `cv2.warpAffine(img, M, (w, h))` | Apply affine transform (rotation) |
| `cv2.rectangle(img, pt1, pt2, color, thickness)` | Draw rectangle |
| `cv2.circle(img, center, radius, color, thickness)` | Draw circle |
| `cv2.line(img, pt1, pt2, color, thickness)` | Draw line |
| `cv2.polylines(img, pts, closed, color, thickness)` | Draw polygon |
| `cv2.putText(img, text, org, font, scale, color, thickness)` | Add text |
| `cv2.convertScaleAbs(img, alpha, beta)` | Adjust brightness/contrast |

---

## 📋 Operations Implemented

| # | Operation | Function |
|---|---|---|
| 1 | Read & display properties | `img.shape`, `os.path.getsize()` |
| 2 | Convert to grayscale | `cv2.COLOR_BGR2GRAY` |
| 3 | Resize to multiple resolutions | `cv2.resize()` |
| 4 | Crop regions (top/bottom/center) | NumPy array slicing `img[y1:y2, x1:x2]` |
| 5 | Rotate 90°, 180°, 270° | `getRotationMatrix2D` + `warpAffine` |
| 6 | Flip H, V, Both | `cv2.flip()` |
| 7 | Draw rect, circle, line, polygon | `cv2.rectangle/circle/line/polylines` |
| 8 | Add custom text | `cv2.putText()` |
| 9 | Save processed images | `cv2.imwrite()` |
| 10 | Brightness & contrast | `cv2.convertScaleAbs()` |
| 11 | BGR vs RGB comparison | `cv2.COLOR_BGR2RGB` |

---

## 🚧 Challenges & Solutions

| Challenge | Solution |
|---|---|
| Images display with wrong colors in matplotlib | Always convert BGR→RGB before `plt.imshow()` |
| Rotation crops corners for non-square images | Used `warpAffine` with original dimensions; for lossless rotation use `cv2.rotate()` |
| `cv2.imshow()` doesn't work in Colab | Used `matplotlib.pyplot.imshow()` instead + `cv2.cvtColor()` for color correction |
| Crop coordinates out of bounds | Used `h//4`, `w//4` fractions of image dimensions for safe cropping |

---

## 📅 Date
**July 6, 2026**

> *"These are the building blocks that every Computer Vision Engineer should know."*
