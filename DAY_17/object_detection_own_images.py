"""
Practice 2 — Test the model on your own images
- Observe detected objects, confidence scores, and bounding boxes

Note: This sandbox environment can't browse the open web to fetch arbitrary
personal photos, so the two Ultralytics sample images are used here as
stand-ins. To use this with your own images, just change IMAGE_PATHS below
to point at your own photo files (e.g. photos on your phone/laptop).
"""

from ultralytics import YOLO

IMAGE_PATHS = [
    "sample_images/zidane.jpg",
    "sample_images/bus.jpg",
]

model = YOLO("yolov8n.pt")

results = model.predict(
    source=IMAGE_PATHS,
    save=True,
    project="outputs",
    name="own_images",
    exist_ok=True
)

for path, result in zip(IMAGE_PATHS, results):
    print(f"\n================  {path}  ================")
    print(f"Number of objects detected: {len(result.boxes)}")

    for box in result.boxes:
        cls_id = int(box.cls[0])
        class_name = model.names[cls_id]
        confidence = float(box.conf[0])
        x1, y1, x2, y2 = [round(v, 1) for v in box.xyxy[0].tolist()]

        print(f"  Object: {class_name:12s} | Confidence: {confidence:.2f} | "
              f"Bounding Box: (x1={x1}, y1={y1}, x2={x2}, y2={y2})")

print("\nAnnotated images saved to outputs/own_images/")
