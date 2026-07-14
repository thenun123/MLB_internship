"""
Mini Project — Object Detection using YOLO
Dataset category: Vehicle Detection

Note on dataset choice: this sandbox environment cannot reach Roboflow
Universe or Kaggle directly (network access is restricted to a small set
of package-hosting domains). Vehicle Detection was chosen specifically
because the pre-trained YOLOv8 model already includes vehicle classes
(car, bus, truck, motorcycle) from the COCO dataset it was trained on, so
meaningful, correct-domain detections are possible on public sample images
without needing a specialized downloaded dataset just to run inference.

To reproduce this with a real downloaded Roboflow/Kaggle vehicle dataset:
1. Download the dataset in YOLO format (images/ + labels/ folders).
2. Point IMAGE_DIR below at that images/ folder instead.
3. Everything else in this script works the same way.
"""

import os
from ultralytics import YOLO

IMAGE_DIR = "sample_images"  # swap this for your downloaded dataset's images/ folder

model = YOLO("yolov8n.pt")

# Vehicle-related classes in the COCO dataset (what YOLOv8n was pretrained on)
VEHICLE_CLASSES = {"car", "bus", "truck", "motorcycle", "bicycle", "train"}

image_files = [
    os.path.join(IMAGE_DIR, f) for f in os.listdir(IMAGE_DIR)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

results = model.predict(
    source=image_files,
    save=True,
    project="outputs",
    name="mini_project_vehicle_detection",
    exist_ok=True
)

print("===== Mini Project: Vehicle Detection Results =====\n")

vehicle_detections = 0
total_detections = 0

for path, result in zip(image_files, results):
    print(f"Image: {path}")
    for box in result.boxes:
        cls_id = int(box.cls[0])
        class_name = model.names[cls_id]
        confidence = float(box.conf[0])
        total_detections += 1

        tag = " <-- VEHICLE" if class_name in VEHICLE_CLASSES else ""
        print(f"  {class_name:12s} | confidence: {confidence:.2f}{tag}")

        if class_name in VEHICLE_CLASSES:
            vehicle_detections += 1
    print()

print(f"Total objects detected across all images: {total_detections}")
print(f"Of which vehicle-class objects: {vehicle_detections}")
print("\nAnnotated output images saved to outputs/mini_project_vehicle_detection/")
