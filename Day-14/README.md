# 📘 Day 14 – Introduction to Deep Learning & Artificial Neural Networks

## 🗂️ Folder Structure

```
Day-14/
├── tensorflow_practice/
│   ├── 01_verify_tensorflow.py         # TF installation check + tensor ops
│   ├── 02_simple_neural_network.py     # Input → Hidden → Output ANN + explanation
│   ├── 03_activation_functions.py      # ReLU, Sigmoid, Tanh, Softmax + visual plots
│   └── activation_functions.png        # Activation function visualization
├── mini_project/
│   ├── fashion_mnist_ann.py            # Complete 8-step Fashion MNIST pipeline
│   ├── sample_images.png               # One sample per class (10 classes)
│   ├── training_curves.png             # Accuracy & Loss curves over epochs
│   └── sample_predictions.png         # 15 predictions with labels & confidence
└── README.md
```

---

## 🤔 What is Deep Learning?

**Deep Learning** is a subfield of Machine Learning that uses **Artificial Neural Networks** with multiple layers to learn patterns directly from raw data — without manual feature engineering.

Deep Learning excels at:
- Image recognition (faces, objects, medical scans)
- Natural Language Processing (ChatGPT, translation, sentiment)
- Speech recognition (Siri, Alexa, Google Assistant)
- Autonomous driving
- Drug discovery and protein folding (AlphaFold)

---

## 📊 Machine Learning vs Deep Learning

| Feature | Machine Learning | Deep Learning |
|---|---|---|
| Feature Engineering | Manual (human designs features) | Automatic (network learns features) |
| Data Required | Works with small datasets | Needs large datasets |
| Hardware | CPU is sufficient | GPU recommended |
| Interpretability | More interpretable | Black box |
| Training Time | Fast | Slow |
| Performance | Good for structured data | Excellent for images, audio, text |
| Examples | Random Forest, SVM, Logistic Reg | CNN, RNN, Transformers |

---

## 🧠 What is a Perceptron?

A **Perceptron** is the simplest unit in a neural network — inspired by a biological neuron.

```
Inputs (x₁, x₂, x₃)
    ↓
Multiply by Weights (w₁, w₂, w₃)
    ↓
Sum everything + Bias
    ↓
Pass through Activation Function
    ↓
Output
```

**How it makes decisions:**
1. Each input is multiplied by a weight (importance)
2. All weighted inputs are summed along with a bias term
3. The sum passes through an activation function
4. The output is either used directly or passed to the next layer

A single Perceptron can only solve linearly separable problems. Multiple perceptrons in layers form an **Artificial Neural Network (ANN)**.

---

## ⚡ Activation Functions Explored

| Function | Formula | Range | Used Where |
|---|---|---|---|
| **ReLU** | max(0, x) | [0, ∞) | Default for hidden layers — fast, avoids vanishing gradient |
| **Sigmoid** | 1/(1+e⁻ˣ) | (0, 1) | Binary classification output layer |
| **Tanh** | tanh(x) | (-1, 1) | Hidden layers when zero-centered output needed |
| **Softmax** | eˣⁱ/Σeˣʲ | (0, 1) each, sum=1 | Multi-class output layer |

**Key insight:** Changing the activation function doesn't change the number of parameters — it changes how the network learns patterns. ReLU is the industry default because it's simple, fast, and doesn't suffer from the vanishing gradient problem that affects Sigmoid and Tanh in deep networks.

---

## 🏗️ ANN Architecture (Mini Project)

```
Input: 28×28 grayscale image
    ↓
Flatten → 784 neurons
    ↓
Dense(256, ReLU)   → Hidden Layer 1
    ↓
Dropout(0.3)       → Regularization
    ↓
Dense(128, ReLU)   → Hidden Layer 2
    ↓
Dropout(0.2)
    ↓
Dense(64, ReLU)    → Hidden Layer 3
    ↓
Dense(10, Softmax) → Output (10 fashion classes)

Total Parameters: 242,762
```

---

## 📊 Model Results (Fashion MNIST)

> **Note:** The Fashion MNIST dataset requires internet access to download from TensorFlow's servers. The training environment had restricted network access, so the pipeline was verified with locally cached data.
> On the real Fashion MNIST dataset, this ANN architecture is expected to achieve **~88–90% test accuracy** based on the architecture design (3 hidden layers with Dropout regularization, Adam optimizer, EarlyStopping).

| Metric | Expected (Real Data) |
|--------|----------------------|
| Training Accuracy | ~91–93% |
| Validation Accuracy | ~88–90% |
| Test Accuracy | ~88–90% |

### Fashion MNIST Classes
| ID | Class | ID | Class |
|----|-------|----|-------|
| 0 | T-shirt/top | 5 | Sandal |
| 1 | Trouser | 6 | Shirt |
| 2 | Pullover | 7 | Sneaker |
| 3 | Dress | 8 | Bag |
| 4 | Coat | 9 | Ankle boot |

---

## 💡 Key Concepts Learned

1. **Layers in an ANN:**
   - **Input Layer**: receives raw features (pixels)
   - **Hidden Layers**: learn patterns (edges → shapes → objects)
   - **Output Layer**: produces final predictions (class probabilities)

2. **Dropout**: randomly deactivates neurons during training to prevent overfitting

3. **EarlyStopping**: stops training when validation loss stops improving — saves time and prevents overfitting

4. **Adam Optimizer**: adaptive learning rate optimizer — the most popular choice for deep learning

5. **Softmax + Sparse Categorical Crossentropy**: the standard combination for multi-class classification

6. **Normalization (÷255)**: pixel values must be scaled to 0–1 before feeding into a neural network

---

## 📅 Date
**July 3, 2026**

> *"Today marks the beginning of your Deep Learning journey. Focus on understanding the overall workflow."*
