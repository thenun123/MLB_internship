# ============================================================
#   Day 21 – Contour Detection Practice
#   - Find contours
#   - Draw contours
#   - Area & Perimeter
#   - Bounding Rectangle
#   - Minimum Enclosing Circle
# ============================================================

import cv2
import numpy as np
import os

INPUT  = '../input_images'
OUTPUT = '../output_images'
os.makedirs(OUTPUT, exist_ok=True)

def show_info(label, value):
    print(f"    {label:<25}: {value}")

# ── Load image ───────────────────────────────────────────────
img  = cv2.imread(os.path.join(INPUT, 'img03_mixed_shapes.png'))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("=" * 55)
print("  CONTOUR DETECTION PRACTICE")
print("=" * 55)
print(f"\n  Image shape: {img.shape}")

# ── Step 1: Threshold ────────────────────────────────────────
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite(os.path.join(OUTPUT, 'practice_01_threshold.png'), thresh)
print("\n✅ Step 1: Threshold applied")

# ── Step 2: Find Contours ────────────────────────────────────
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
print(f"✅ Step 2: Found {len(contours)} contours")

# ── Step 3: Draw All Contours ────────────────────────────────
all_contours = img.copy()
cv2.drawContours(all_contours, contours, -1, (0, 255, 0), 2)
cv2.imwrite(os.path.join(OUTPUT, 'practice_02_all_contours.png'), all_contours)
print("✅ Step 3: All contours drawn (green)")

# ── Step 4: Area & Perimeter ─────────────────────────────────
print("\n  Contour Properties:")
print(f"  {'#':<4} {'Area':>10} {'Perimeter':>12} {'Aspect Ratio':>14}")
print("  " + "-" * 42)

for i, cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    if area < 500:
        continue
    peri  = cv2.arcLength(cnt, True)
    x,y,w,h = cv2.boundingRect(cnt)
    ar    = round(w/h, 2)
    print(f"  {i+1:<4} {area:>10.1f} {peri:>12.1f} {ar:>14}")

# ── Step 5: Bounding Rectangles ──────────────────────────────
bounding = img.copy()
for cnt in contours:
    if cv2.contourArea(cnt) < 500:
        continue
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(bounding, (x, y), (x+w, y+h), (0, 0, 255), 2)
cv2.imwrite(os.path.join(OUTPUT, 'practice_03_bounding_rect.png'), bounding)
print("\n✅ Step 5: Bounding rectangles drawn (red)")

# ── Step 6: Minimum Enclosing Circle ─────────────────────────
enclosing = img.copy()
for cnt in contours:
    if cv2.contourArea(cnt) < 500:
        continue
    (cx, cy), radius = cv2.minEnclosingCircle(cnt)
    cv2.circle(enclosing, (int(cx), int(cy)), int(radius), (255, 0, 0), 2)
    cv2.circle(enclosing, (int(cx), int(cy)), 4, (255, 0, 0), -1)
cv2.imwrite(os.path.join(OUTPUT, 'practice_04_enclosing_circle.png'), enclosing)
print("✅ Step 6: Minimum enclosing circles drawn (blue)")

# ── Step 7: Combined Output ──────────────────────────────────
combined = img.copy()
for cnt in contours:
    if cv2.contourArea(cnt) < 500:
        continue
    # Green contour
    cv2.drawContours(combined, [cnt], -1, (0, 255, 0), 2)
    # Red bounding rect
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(combined, (x, y), (x+w, y+h), (0, 0, 255), 2)
    # Blue enclosing circle
    (cx, cy), r = cv2.minEnclosingCircle(cnt)
    cv2.circle(combined, (int(cx), int(cy)), int(r), (255, 0, 0), 2)
    # Area label
    area = cv2.contourArea(cnt)
    cv2.putText(combined, f'A={int(area)}',
                (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0,0,0), 1)

cv2.imwrite(os.path.join(OUTPUT, 'practice_05_combined.png'), combined)
print("✅ Step 7: Combined output saved")

print("\n✅ All practice outputs saved to output_images/")
