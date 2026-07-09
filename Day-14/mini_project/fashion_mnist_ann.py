# ============================================================
#    👗  FASHION MNIST – ARTIFICIAL NEURAL NETWORK
#        Mini Project – Day 14
# ============================================================
# Classes:
#   0: T-shirt/top   1: Trouser     2: Pullover
#   3: Dress         4: Coat        5: Sandal
#   6: Shirt         7: Sneaker     8: Bag
#   9: Ankle boot
# ============================================================

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, Input
from tensorflow.keras.callbacks import EarlyStopping

CLASS_NAMES = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

print("=" * 62)
print("    👗  FASHION MNIST – ARTIFICIAL NEURAL NETWORK  👗")
print("=" * 62)

# ── STEP 1: Load Dataset ─────────────────────────────────────
print("\n📦 STEP 1: Loading Fashion MNIST Dataset...")
try:
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    print("  ✅ Loaded from TensorFlow/Keras built-in datasets")
except Exception:
    print("  ⚠️  Online fetch blocked – loading local cached data...")
    X_train = np.load('/home/claude/fmnist_X_train.npy')
    y_train = np.load('/home/claude/fmnist_y_train.npy')
    X_test  = np.load('/home/claude/fmnist_X_test.npy')
    y_test  = np.load('/home/claude/fmnist_y_test.npy')
    print("  ✅ Loaded from local cache")

print(f"  Training images : {X_train.shape}")
print(f"  Test images     : {X_test.shape}")
print(f"  Pixel range     : {X_train.min()} to {X_train.max()}")

print(f"\n  Class Distribution (train):")
for i, name in enumerate(CLASS_NAMES):
    count = np.sum(y_train == i)
    print(f"    [{i}] {name:<15} : {count} images")

# ── STEP 2: Visualize Sample Images ──────────────────────────
print(f"\n🖼️  STEP 2: Saving Sample Images...")
fig, axes = plt.subplots(2, 5, figsize=(13, 6))
fig.suptitle('Fashion MNIST – Sample Images (one per class)',
             fontsize=13, fontweight='bold')
for i in range(10):
    idx = np.where(y_train == i)[0][0]
    ax  = axes[i // 5][i % 5]
    ax.imshow(X_train[idx], cmap='gray')
    ax.set_title(f'[{i}] {CLASS_NAMES[i]}', fontsize=9)
    ax.axis('off')
plt.tight_layout()
plt.savefig('sample_images.png', dpi=150, bbox_inches='tight')
print("  ✅ Saved: sample_images.png")

# ── STEP 3: Normalize ────────────────────────────────────────
print(f"\n🔧 STEP 3: Normalizing Pixel Values (0-255 -> 0.0-1.0)...")
X_train = X_train / 255.0
X_test  = X_test  / 255.0
print(f"  New pixel range : {X_train.min():.1f} to {X_train.max():.1f}  ✅")

# ── STEP 4: Build ANN ────────────────────────────────────────
print(f"\n🏗️  STEP 4: Building Artificial Neural Network...")

model = Sequential([
    Input(shape=(28, 28)),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.3),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(64,  activation='relu'),
    Dense(10,  activation='softmax')
], name="FashionMNIST_ANN")

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("\n  Model Summary:")
model.summary()
print(f"\n  Total Parameters: {model.count_params():,}")

# ── STEP 5: Train ────────────────────────────────────────────
print(f"\n🚀 STEP 5: Training the Model (up to 20 epochs)...")
early_stop = EarlyStopping(monitor='val_loss', patience=3,
                           restore_best_weights=True, verbose=0)

history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=128,
    validation_split=0.1,
    callbacks=[early_stop],
    verbose=1
)

epochs_ran = len(history.history['loss'])
print(f"\n  ✅ Training complete! Ran {epochs_ran} epochs.")

# ── STEP 6: Evaluate ─────────────────────────────────────────
print(f"\n📊 STEP 6: Evaluating on Test Set...")
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
train_acc = history.history['accuracy'][-1]
val_acc   = history.history['val_accuracy'][-1]

print(f"\n  {'Metric':<25} {'Value':>10}")
print(f"  {'-' * 37}")
print(f"  {'Final Training Accuracy':<25} {train_acc*100:>9.2f}%")
print(f"  {'Final Validation Accuracy':<25} {val_acc*100:>9.2f}%")
print(f"  {'Test Accuracy':<25} {test_acc*100:>9.2f}%")
print(f"  {'Test Loss':<25} {test_loss:>10.4f}")

# ── STEP 7: Training Curves ──────────────────────────────────
print(f"\n📈 STEP 7: Plotting Training Curves...")
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('Fashion MNIST – Training History', fontsize=13, fontweight='bold')

ep = range(1, epochs_ran + 1)

axes[0].plot(ep, history.history['accuracy'],     'b-o', markersize=4, label='Train Acc')
axes[0].plot(ep, history.history['val_accuracy'], 'r-o', markersize=4, label='Val Acc')
axes[0].axhline(y=test_acc, color='green', linestyle='--', label=f'Test Acc={test_acc*100:.1f}%')
axes[0].set_title('Model Accuracy', fontweight='bold')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Accuracy')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(ep, history.history['loss'],     'b-o', markersize=4, label='Train Loss')
axes[1].plot(ep, history.history['val_loss'], 'r-o', markersize=4, label='Val Loss')
axes[1].set_title('Model Loss', fontweight='bold')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Loss')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('training_curves.png', dpi=150, bbox_inches='tight')
print("  ✅ Saved: training_curves.png")

# ── STEP 8: Predictions ──────────────────────────────────────
print(f"\n🔍 STEP 8: Sample Predictions (15 images)...")
y_pred_probs = model.predict(X_test[:15], verbose=0)
y_pred       = np.argmax(y_pred_probs, axis=1)

fig, axes = plt.subplots(3, 5, figsize=(15, 9))
fig.suptitle(f'Fashion MNIST – Sample Predictions  (Test Acc: {test_acc*100:.2f}%)',
             fontsize=13, fontweight='bold')

for i, ax in enumerate(axes.flat):
    ax.imshow(X_test[i], cmap='gray')
    pred   = CLASS_NAMES[y_pred[i]]
    actual = CLASS_NAMES[y_test[i]]
    conf   = y_pred_probs[i][y_pred[i]] * 100
    correct = y_pred[i] == y_test[i]
    color  = 'green' if correct else 'red'
    mark   = 'CORRECT' if correct else 'WRONG'
    ax.set_title(f'[{mark}]\nPred: {pred}\nActual: {actual}\nConf: {conf:.1f}%',
                 fontsize=7.5, color=color)
    ax.axis('off')

plt.tight_layout()
plt.savefig('sample_predictions.png', dpi=150, bbox_inches='tight')
print("  ✅ Saved: sample_predictions.png")

# ── Console Table ─────────────────────────────────────────────
print(f"\n  {'#':<4} {'Actual':<16} {'Predicted':<16} {'Confidence':>10} {'Result'}")
print(f"  {'-' * 58}")
for i in range(15):
    actual    = CLASS_NAMES[y_test[i]]
    predicted = CLASS_NAMES[y_pred[i]]
    conf      = y_pred_probs[i][y_pred[i]] * 100
    result    = "✅" if y_pred[i] == y_test[i] else "❌"
    print(f"  {i+1:<4} {actual:<16} {predicted:<16} {conf:>9.1f}% {result}")

correct_count = np.sum(y_pred == y_test[:15])
print(f"\n  Correct: {correct_count}/15  ({correct_count/15*100:.1f}%)")

print(f"\n{'=' * 62}")
print(f"  ✅  Fashion MNIST ANN Training Complete!")
print(f"  Final Test Accuracy : {test_acc*100:.2f}%")
print(f"{'=' * 62}")
