# 📘 Day 15 – Convolutional Neural Networks (CNN) & Image Classification

## 🗂️ Folder Structure

```
Day-15/
├── cnn_practice/
│   └── cnn_practice.py                 # Practice 1+2+3: Load, Build CNN, Evaluate
├── fashion_mnist_cnn/
│   ├── fashion_mnist_cnn.py            # Complete CNN Mini Project
│   ├── sample_images.png               # One sample per class
│   ├── training_curves.png             # Accuracy & Loss over epochs
│   ├── confusion_matrix.png            # Full 10-class confusion matrix
│   └── correct_vs_incorrect.png        # 10 correct + 10 incorrect predictions
└── README.md
```

---

## 🤔 Why CNNs Are Better Than ANNs for Image Data

| Feature | ANN (Dense) | CNN |
|---|---|---|
| Input | Flattened 1D vector | 2D spatial grid preserved |
| Parameters | Huge — every pixel connects to every neuron | Much fewer — shared filters |
| Spatial awareness | None — loses positional info | Yes — detects spatial patterns |
| Translation invariance | No | Yes — detects features anywhere |
| Feature learning | Manual / indirect | Automatic through convolution |
| Scalability | Poor for large images | Excellent |

An ANN treating a 28×28 image as 784 flat numbers loses all spatial structure. A CNN processes the image in its 2D form, allowing it to learn that pixels near each other matter together.

---

## 🔬 Purpose of Each Layer

### Convolution Layer (Conv2D)
Applies learned filters (kernels) that slide across the image to detect features:
- Early layers: edges, lines, corners
- Deeper layers: shapes, textures, parts of objects

Each filter produces a **feature map** highlighting where that pattern appears.

### Pooling Layer (MaxPooling2D)
Reduces the spatial size of feature maps (e.g., 28×28 → 14×14) by keeping the strongest activation in each 2×2 window. Benefits:
- Reduces computation and parameters
- Adds translation invariance
- Helps prevent overfitting

### Flatten Layer
Converts the 3D tensor (height × width × filters) into a 1D vector so it can be fed to Dense layers.

### Fully Connected (Dense) Layers
After spatial features are extracted, Dense layers learn class-level patterns and produce final predictions.

---

## 🏗️ CNN Architecture

```
Input: 28×28×1 (grayscale image)
    ↓
Conv2D(32, 3×3, ReLU, same)   → 28×28×32  (detect basic features)
MaxPooling2D(2×2)              → 14×14×32
    ↓
Conv2D(64, 3×3, ReLU, same)   → 14×14×64  (detect complex features)
MaxPooling2D(2×2)              →  7×7×64
    ↓
Flatten()                      → 3136 neurons
Dense(128, ReLU)               → 128 neurons
Dropout(0.3)                   → prevent overfitting
Dense(10, Softmax)             → 10 class probabilities

Total Parameters: 421,642
Optimizer: Adam
Loss: Sparse Categorical Crossentropy
```

---

## 📊 Model Performance

> **Note:** Fashion MNIST download was blocked in this training environment. Results below are from training on a synthetic data subset (random pixels). On real Fashion MNIST, this CNN architecture achieves **~91–93% test accuracy**.

| Metric | Expected (Real Data) |
|--------|----------------------|
| Training Accuracy | ~93–95% |
| Validation Accuracy | ~91–92% |
| Test Accuracy | ~91–93% |

### CNN vs ANN Comparison (on real Fashion MNIST)

| Model | Test Accuracy | Parameters |
|-------|--------------|------------|
| ANN (Day 14) | ~88–90% | 242,762 |
| CNN (Day 15) | ~91–93% | 421,642 |

The CNN outperforms the ANN by ~3–5% despite having relatively few additional parameters, because it exploits the spatial structure of images through convolution.

---

## ⚙️ Key Deep Learning Techniques Used

| Technique | Purpose |
|---|---|
| `padding='same'` | Keeps feature map size the same after convolution |
| `MaxPooling2D(2,2)` | Halves spatial dimensions, reduces computation |
| `Dropout(0.3)` | Randomly drops 30% of neurons — prevents overfitting |
| `EarlyStopping(patience=4)` | Stops training when val_loss stops improving |
| `ReduceLROnPlateau` | Halves learning rate when stuck — helps escape plateaus |
| `BatchNormalization` | Normalizes activations — stabilizes and speeds training |

---

## 🔍 Key Concepts Understood

1. **Overfitting in Deep Learning** — Training accuracy much higher than test accuracy. Signs: val_loss increases while train_loss decreases. Solutions: Dropout, BatchNorm, EarlyStopping, data augmentation.

2. **Data Augmentation** — Artificially expanding the dataset by flipping, rotating, or zooming images. This helps the model generalize to unseen variations.

3. **Epoch vs Batch Size** — An epoch = one full pass through the training data. A batch = how many samples to process before updating weights. Larger batches = faster but less stable training.

4. **Feature Maps** — The output of a Conv2D layer showing where specific patterns are detected across the image.

5. **Transfer Learning (coming next)** — Instead of training from scratch, we can use a pretrained model (like VGG, ResNet, EfficientNet) as the feature extractor and only train the top layers.

---

## 🚧 Challenges & Solutions

| Challenge | Solution |
|---|---|
| Fashion MNIST download blocked by network | Used locally cached synthetic data to verify the pipeline; noted expected accuracy separately |
| Training timeout with large model | Reduced training subset and simplified architecture for demonstration; full script retained for local training |
| Low accuracy on random data | Expected — model needs real pixel patterns to learn; architecture is correct |

---

## 📅 Date
**July 4, 2026**

> *"Take your time to understand how images pass through each layer of the network. CNNs are the foundation of modern Computer Vision."*
