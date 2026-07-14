"""
Practice 1 — Ultralytics YOLO Basic Usage
- Load a pre-trained YOLO model
- Run object detection on a single image
- Run object detection on multiple images
- Save the prediction results
"""

from ultralytics import YOLO

# -----------------------------
# 1. Load a pre-trained YOLO model
# -----------------------------
# YOLOv8n = the "nano" version: smallest and fastest, good for quick practice/testing
model = YOLO("yolov8n.pt")

print("Model loaded. Classes it can detect:")
print(model.names)

# -----------------------------
# 2. Object detection on a single image
# -----------------------------
single_result = model.predict(
    source="sample_images/zidane.jpg",
    save=True,
    project="outputs",
    name="single_image",
    exist_ok=True
)

print("\n--- Single Image Results (zidane.jpg) ---")
for box in single_result[0].boxes:
    cls_id = int(box.cls[0])
    conf = float(box.conf[0])
    xyxy = box.xyxy[0].tolist()
    print(f"Detected: {model.names[cls_id]:15s} | Confidence: {conf:.2f} | Box: {[round(v, 1) for v in xyxy]}")

# -----------------------------
# 3. Object detection on multiple images
# -----------------------------
image_list = ["sample_images/zidane.jpg", "sample_images/bus.jpg"]

multi_results = model.predict(
    source=image_list,
    save=True,
    project="outputs",
    name="multiple_images",
    exist_ok=True
)

print("\n--- Multiple Image Results ---")
for i, result in enumerate(multi_results):
    print(f"\nImage: {image_list[i]}")
    for box in result.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        print(f"  Detected: {model.names[cls_id]:15s} | Confidence: {conf:.2f}")

print("\nAll results saved under the 'outputs/' folder.")
