# ============================================================
#   Practice 2: Build a Simple Neural Network
#               Input → Hidden → Output
# ============================================================

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Input

print("=" * 55)
print("     SIMPLE NEURAL NETWORK – STRUCTURE DEMO")
print("=" * 55)

# ── Build the Model ──────────────────────────────────────────
# Problem: Classify handwritten digits (10 classes)
# Input : 784 features (28×28 pixels flattened)

model = Sequential([
    Input(shape=(784,)),             # Input Layer  – 784 neurons (one per pixel)
    Dense(128, activation='relu'),   # Hidden Layer – 128 neurons, ReLU activation
    Dense(10,  activation='softmax') # Output Layer – 10 neurons (one per digit class)
], name="Simple_ANN")

# ── Print Summary ────────────────────────────────────────────
print("\n📋 Model Summary:")
model.summary()

# ── Explain Each Layer ───────────────────────────────────────
print("\n📚 Layer-by-Layer Explanation:")
print("─" * 55)
print("""
  1. INPUT LAYER (784 neurons)
     - Receives raw data: one neuron per pixel value (28×28=784)
     - No computation happens here; it just passes data forward
     - Each neuron holds a value between 0 (black) and 255 (white)

  2. HIDDEN LAYER (128 neurons, ReLU)
     - The "thinking" layer — where patterns are learned
     - Each neuron is connected to all 784 input neurons
     - ReLU activation: outputs 0 if input < 0, else outputs the value
     - Parameters: 784×128 weights + 128 biases = 100,480

  3. OUTPUT LAYER (10 neurons, Softmax)
     - One neuron per class (digits 0–9)
     - Softmax converts raw scores to probabilities (sum = 1.0)
     - The neuron with the highest probability = predicted class
     - Parameters: 128×10 weights + 10 biases = 1,290
""")

total_params = model.count_params()
print(f"  Total Trainable Parameters : {total_params:,}")
print(f"  That means the network has {total_params:,} values it learns!")
print("─" * 55)
