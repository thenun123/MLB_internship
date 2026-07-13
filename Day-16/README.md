# 📘 Day 16 – Transfer Learning with MobileNetV2

## 🗂️ Folder Structure

```
Day-16/
├── transfer_learning_practice/
│   ├── 01_mobilenetv2_exploration.py   # Load, freeze, add custom head
│   └── 02_model_comparison.py          # VGG16 vs ResNet50 vs MobileNetV2 vs EfficientNetB0
├── cats_vs_dogs_classifier/
│   └── cats_vs_dogs_transfer.py        # Full mini project pipeline
└── README.md
```

---

## 🤔 What is Transfer Learning?

Transfer Learning is a technique where a model trained on one large dataset (like ImageNet with 1.2M images and 1000 classes) is reused as the starting point for a different but related task.

Instead of training from scratch, we:
1. Take a pre-trained model (e.g., MobileNetV2 trained on ImageNet)
2. **Freeze** the base layers — they already know useful features (edges, shapes, textures)
3. Add our own **classification head** on top
4. Train only the new head on our specific data

**Why it works:** Low-level visual features (edges, curves, textures) are universal across image tasks. A model that learned them on 1.2M images transfers that knowledge to cats vs dogs instantly.

---

## 🎯 Why MobileNetV2?

| Model | Parameters | Reason Chosen |
|-------|-----------|---------------|
| VGG16 | 138M | Too large, slow to train |
| ResNet50 | 25M | Good accuracy but heavier |
| **MobileNetV2** | **2.3M** | ✅ Lightweight, fast, 93–97% accuracy |
| EfficientNetB0 | 5.3M | Great, but MobileNetV2 is simpler for learning |

MobileNetV2 uses **depthwise separable convolutions** which are 8–9× faster than standard convolutions while maintaining near-identical accuracy. It's the industry standard for mobile and edge deployment.

---

## 🏗️ Model Architecture

```
Input: 160×160×3
    ↓
MobileNetV2 (FROZEN — 154 layers, ImageNet weights)
  Knows: edges → shapes → textures → object parts
    ↓
GlobalAveragePooling2D
  Converts 5×5×1280 feature map → 1280 vector
    ↓
Dense(256, ReLU) + Dropout(0.4)
  Learns cat vs dog discrimination
    ↓
Dense(1, Sigmoid)
  Output: P(Dog)  — >0.5 = Dog, ≤0.5 = Cat

Total Parameters  : ~2.58M
Trainable (Phase 1): ~328K  (head only — 12.7%)
Trainable (Phase 2): ~1.2M  (head + top 30 base layers)
```

---

## 🔬 Training Strategy

### Phase 1 – Feature Extraction
- Base model: **fully frozen**
- Only the classification head is trained
- Learning rate: `1e-3`
- Epochs: up to 20 (with EarlyStopping)
- Purpose: Let the head adapt to cat/dog features quickly

### Phase 2 – Fine-Tuning
- Unfreeze **top 30 layers** of MobileNetV2
- Keep lower layers frozen (they have universal features)
- Learning rate: `1e-5` (very low, to avoid destroying learned weights)
- Epochs: up to 10
- Purpose: Squeeze extra accuracy by adapting top layers to this specific task

---

## 📊 Experiments & Observations

| Experiment | Val Accuracy | Notes |
|---|---|---|
| Feature extraction only (no augmentation) | ~88% | Baseline |
| + Data augmentation (flip, brightness, contrast) | ~91% | Improved generalization |
| + Fine-tuning top 30 layers | ~93–97% | Best result |
| ReduceLROnPlateau added | More stable | Avoids loss plateaus |

**Key findings:**
- Fine-tuning alone without Phase 1 first caused instability — always warm up the head first
- Very low LR (`1e-5`) in Phase 2 is critical — high LR destroys the pretrained weights
- `GlobalAveragePooling2D` outperforms `Flatten` here — fewer params, less overfitting
- Data augmentation prevents overfitting on the ~18,700 training images

---

## 💡 Transfer Learning vs Training from Scratch

| Aspect | From Scratch | Transfer Learning |
|---|---|---|
| Data needed | Millions of images | Thousands |
| Training time | Hours / Days | Minutes |
| Final accuracy | ~85% (on 18K images) | 93–97% |
| GPU required | Yes | Not necessarily |
| Industry use | Rare | Standard practice |

---

## 📅 Date
**July 5, 2026**

> *"Transfer Learning is one of the most commonly used approaches in real-world AI projects. Focus on understanding the workflow."*
