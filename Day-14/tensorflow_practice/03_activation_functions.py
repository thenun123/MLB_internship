# ============================================================
#   Practice 3: Activation Functions – ReLU, Sigmoid, Tanh
# ============================================================

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Input

print("=" * 58)
print("     ACTIVATION FUNCTIONS – EXPLORATION")
print("=" * 58)

# ── Visualize Activation Functions ───────────────────────────
x = np.linspace(-5, 5, 300)

def relu(x):    return np.maximum(0, x)
def sigmoid(x): return 1 / (1 + np.exp(-x))
def tanh(x):    return np.tanh(x)
def softmax(x):
    e = np.exp(x - np.max(x))
    return e / e.sum()

fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.suptitle('Activation Functions – Visual Comparison', fontsize=14, fontweight='bold')

configs = [
    (axes[0,0], relu,    '#e74c3c', 'ReLU (Rectified Linear Unit)',
     'f(x) = max(0, x)',
     'Best for hidden layers.\nFast, avoids vanishing gradient.\nMost widely used.'),
    (axes[0,1], sigmoid, '#2ecc71', 'Sigmoid',
     'f(x) = 1 / (1 + e^(-x))',
     'Output in (0, 1).\nUsed in binary classification output.\nCan cause vanishing gradient.'),
    (axes[1,0], tanh,    '#3498db', 'Tanh (Hyperbolic Tangent)',
     'f(x) = tanh(x)',
     'Output in (-1, 1).\nZero-centered (better than sigmoid).\nStill has vanishing gradient issue.'),
    (axes[1,1], softmax, '#f39c12', 'Softmax',
     'f(xᵢ) = e^xᵢ / Σe^xⱼ',
     'Converts scores to probabilities.\nSum of outputs = 1.0.\nUsed in multi-class output layer.'),
]

for ax, fn, color, title, formula, notes in configs:
    if fn == softmax:
        y = softmax(x)
    else:
        y = fn(x)
    ax.plot(x, y, color=color, linewidth=2.5)
    ax.axhline(0, color='gray', linewidth=0.8, linestyle='--')
    ax.axvline(0, color='gray', linewidth=0.8, linestyle='--')
    ax.set_title(title, fontweight='bold', fontsize=11)
    ax.set_xlabel('Input (x)')
    ax.set_ylabel('Output f(x)')
    ax.text(0.02, 0.95, formula, transform=ax.transAxes,
            fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    ax.text(0.02, 0.05, notes, transform=ax.transAxes,
            fontsize=8, verticalalignment='bottom', color='gray')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('activation_functions.png', dpi=150, bbox_inches='tight')
print("\n✅ Saved: activation_functions.png")

# ── Build Models with Different Activations ──────────────────
print("\n📐 Model Structures with Different Activation Functions:")
print("─" * 58)

for activation in ['relu', 'sigmoid', 'tanh']:
    m = Sequential([
        Input(shape=(784,)),
        Dense(128, activation=activation),
        Dense(64,  activation=activation),
        Dense(10,  activation='softmax')
    ])
    params = m.count_params()
    print(f"\n  🔹 Activation: {activation.upper()}")
    print(f"     Hidden layers  : 2 (128 → 64 neurons)")
    print(f"     Total params   : {params:,}")
    print(f"     Output layer   : softmax (always for multi-class)")

print("\n─" * 58)
print("""
📝 Key Observations:
  - Changing activation doesn't change parameter count
  - ReLU is the default choice for hidden layers (fast + effective)
  - Sigmoid/Tanh can suffer from vanishing gradients in deep networks
  - Softmax is always used in the output layer for classification
  - The same architecture with different activations learns differently
""")
