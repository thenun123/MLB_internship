# ============================================================
#   CNN Practice – Fashion MNIST
#   Practice 1: Load & Visualize
#   Practice 2: Build CNN
#   Practice 3: Evaluate
# ============================================================

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input
)

CLASS_NAMES = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

# ── PRACTICE 1: Load & Visualize ─────────────────────────────
print("=" * 55)
print("  PRACTICE 1: Load, Visualize & Normalize")
print("=" * 55)

try:
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    print("✅ Loaded from TF/Keras")
except Exception:
    print("⚠️  Loading from local cache...")
    X_train = np.load('/home/claude/fmnist_X_train.npy')
    y_train = np.load('/home/claude/fmnist_y_train.npy')
    X_test  = np.load('/home/claude/fmnist_X_test.npy')
    y_test  = np.load('/home/claude/fmnist_y_test.npy')

print(f"  Train shape : {X_train.shape}")
print(f"  Test shape  : {X_test.shape}")
print(f"  Pixel range : {X_train.min()} – {X_train.max()}")

# Visualize 10 samples
fig, axes = plt.subplots(2, 5, figsize=(13, 6))
fig.suptitle('Fashion MNIST – 10 Sample Images', fontsize=13, fontweight='bold')
for i, ax in enumerate(axes.flat):
    idx = np.where(y_train == i)[0][0]
    ax.imshow(X_train[idx], cmap='gray')
    ax.set_title(f'[{i}] {CLASS_NAMES[i]}', fontsize=9)
    ax.axis('off')
plt.tight_layout()
plt.savefig('practice1_samples.png', dpi=150, bbox_inches='tight')
print("✅ Saved: practice1_samples.png")

# Normalize
X_train = X_train / 255.0
X_test  = X_test  / 255.0
# Reshape for CNN: (N, 28, 28) → (N, 28, 28, 1)
X_train = X_train[..., np.newaxis]
X_test  = X_test[...,  np.newaxis]
print(f"  After reshape: {X_train.shape}  (added channel dim)")
print(f"  Pixel range after norm: {X_train.min():.1f} – {X_train.max():.1f}")

# ── PRACTICE 2: Build CNN ─────────────────────────────────────
print("\n" + "=" * 55)
print("  PRACTICE 2: Build CNN")
print("=" * 55)

model = Sequential([
    Input(shape=(28, 28, 1)),

    # --- Conv Block 1 ---
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    MaxPooling2D(2, 2),

    # --- Conv Block 2 ---
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    MaxPooling2D(2, 2),

    # --- Classifier Head ---
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(10, activation='softmax')
], name="Fashion_CNN")

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.summary()
print(f"\n  Total Parameters: {model.count_params():,}")

print("\n📚 Layer Explanation:")
print("""
  Conv2D(32, 3×3, ReLU)   → Applies 32 filters to detect low-level features
                             (edges, curves, textures). Output: 28×28×32
  MaxPooling2D(2×2)        → Shrinks spatial size by half. Output: 14×14×32
                             Keeps the strongest activated feature in each 2×2 window.

  Conv2D(64, 3×3, ReLU)   → 64 filters on top of previous — learns complex shapes
                             Output: 14×14×64
  MaxPooling2D(2×2)        → Shrinks again. Output: 7×7×64

  Flatten()                → 7×7×64 = 3136 values into a 1D vector
  Dense(128, ReLU)         → Fully connected layer — learns class patterns
  Dropout(0.3)             → Randomly disables 30% of neurons → prevents overfitting
  Dense(10, Softmax)       → One probability per class; all sum to 1.0
""")

# ── PRACTICE 3: Train & Evaluate ─────────────────────────────
print("=" * 55)
print("  PRACTICE 3: Train & Evaluate")
print("=" * 55)

from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(monitor='val_loss', patience=3,
                           restore_best_weights=True, verbose=0)

history = model.fit(
    X_train, y_train,
    epochs=15,
    batch_size=128,
    validation_split=0.1,
    callbacks=[early_stop],
    verbose=1
)

epochs_ran = len(history.history['loss'])
print(f"\n✅ Training complete! Ran {epochs_ran} epochs.")

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
train_acc = history.history['accuracy'][-1]
val_acc   = history.history['val_accuracy'][-1]

print(f"\n  Training Accuracy   : {train_acc * 100:.2f}%")
print(f"  Validation Accuracy : {val_acc   * 100:.2f}%")
print(f"  Test Accuracy       : {test_acc  * 100:.2f}%")
print(f"  Test Loss           : {test_loss:.4f}")

# Accuracy & Loss curves
ep = range(1, epochs_ran + 1)
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('CNN Practice – Training History', fontsize=13, fontweight='bold')

axes[0].plot(ep, history.history['accuracy'],     'b-o', markersize=4, label='Train')
axes[0].plot(ep, history.history['val_accuracy'], 'r-o', markersize=4, label='Val')
axes[0].axhline(y=test_acc, color='green', linestyle='--', label=f'Test={test_acc*100:.1f}%')
axes[0].set_title('Accuracy')
axes[0].set_xlabel('Epoch'); axes[0].set_ylabel('Accuracy')
axes[0].legend(); axes[0].grid(True, alpha=0.3)

axes[1].plot(ep, history.history['loss'],     'b-o', markersize=4, label='Train')
axes[1].plot(ep, history.history['val_loss'], 'r-o', markersize=4, label='Val')
axes[1].set_title('Loss')
axes[1].set_xlabel('Epoch'); axes[1].set_ylabel('Loss')
axes[1].legend(); axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('practice3_training_curves.png', dpi=150, bbox_inches='tight')
print("✅ Saved: practice3_training_curves.png")

# Sample predictions
y_pred = np.argmax(model.predict(X_test[:10], verbose=0), axis=1)
print(f"\n  Sample Predictions (first 10 test images):")
print(f"  {'Actual':<20} {'Predicted':<20} {'Result'}")
print(f"  {'-'*48}")
for a, p in zip(y_test[:10], y_pred):
    mark = "✅" if a == p else "❌"
    print(f"  {CLASS_NAMES[a]:<20} {CLASS_NAMES[p]:<20} {mark}")
