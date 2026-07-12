# ============================================================
#   👗  FASHION MNIST IMAGE CLASSIFIER – CNN
#       Mini Project – Day 15
# ============================================================

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, AveragePooling2D,
    Flatten, Dense, Dropout, BatchNormalization, Input
)
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.metrics import confusion_matrix, classification_report

CLASS_NAMES = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

print("=" * 64)
print("   👗  FASHION MNIST CNN IMAGE CLASSIFIER  👗")
print("=" * 64)

# ── STEP 1: Load Dataset ─────────────────────────────────────
print("\n📦 STEP 1: Loading Fashion MNIST...")
try:
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    print("  ✅ Loaded from TF/Keras")
except Exception:
    print("  ⚠️  Online blocked – loading from local cache...")
    X_train = np.load('/home/claude/fmnist_X_train.npy')
    y_train = np.load('/home/claude/fmnist_y_train.npy')
    X_test  = np.load('/home/claude/fmnist_X_test.npy')
    y_test  = np.load('/home/claude/fmnist_y_test.npy')

print(f"  Train : {X_train.shape[0]} images  |  Test : {X_test.shape[0]} images")
print(f"  Image size : {X_train.shape[1]}×{X_train.shape[2]} grayscale")

# ── STEP 2: Display Samples ──────────────────────────────────
print(f"\n🖼️  STEP 2: Displaying Sample Images...")
fig, axes = plt.subplots(2, 5, figsize=(13, 6))
fig.suptitle('Fashion MNIST – One Sample Per Class', fontsize=13, fontweight='bold')
for i, ax in enumerate(axes.flat):
    idx = np.where(y_train == i)[0][0]
    ax.imshow(X_train[idx], cmap='gray')
    ax.set_title(f'[{i}] {CLASS_NAMES[i]}', fontsize=9)
    ax.axis('off')
plt.tight_layout()
plt.savefig('sample_images.png', dpi=150, bbox_inches='tight')
print("  ✅ Saved: sample_images.png")

# ── STEP 3: Preprocess ───────────────────────────────────────
print(f"\n🔧 STEP 3: Preprocessing...")
X_train = X_train / 255.0
X_test  = X_test  / 255.0
X_train = X_train[..., np.newaxis]   # (60000, 28, 28, 1)
X_test  = X_test[...,  np.newaxis]
print(f"  Normalized: 0–255 → 0.0–1.0 ✅")
print(f"  Reshaped for CNN: {X_train.shape} ✅")

# ── STEP 4: Build CNN ─────────────────────────────────────────
print(f"\n🏗️  STEP 4: Building CNN Architecture...")

model = Sequential([
    Input(shape=(28, 28, 1)),

    # Conv Block 1: detect basic features (edges, lines)
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    BatchNormalization(),
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    MaxPooling2D(2, 2),
    Dropout(0.25),

    # Conv Block 2: detect complex features (shapes, textures)
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    BatchNormalization(),
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    MaxPooling2D(2, 2),
    Dropout(0.25),

    # Classifier Head
    Flatten(),
    Dense(256, activation='relu'),
    BatchNormalization(),
    Dropout(0.4),
    Dense(10, activation='softmax')
], name="FashionCNN")

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("\n  Model Summary:")
model.summary()
print(f"\n  Total Parameters : {model.count_params():,}")

# ── STEP 5: Train ────────────────────────────────────────────
print(f"\n🚀 STEP 5: Training CNN (up to 20 epochs)...")

callbacks = [
    EarlyStopping(monitor='val_loss', patience=4,
                  restore_best_weights=True, verbose=0),
    ReduceLROnPlateau(monitor='val_loss', factor=0.5,
                      patience=2, verbose=0, min_lr=1e-6)
]

history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=128,
    validation_split=0.1,
    callbacks=callbacks,
    verbose=1
)

epochs_ran = len(history.history['loss'])
print(f"\n  ✅ Training complete! Ran {epochs_ran} epochs.")

# ── STEP 6: Evaluate ─────────────────────────────────────────
print(f"\n📊 STEP 6: Evaluation Results")
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
train_acc = history.history['accuracy'][-1]
val_acc   = history.history['val_accuracy'][-1]

print(f"\n  {'Metric':<25} {'Value':>10}")
print(f"  {'-'*37}")
print(f"  {'Training Accuracy':<25} {train_acc*100:>9.2f}%")
print(f"  {'Validation Accuracy':<25} {val_acc*100:>9.2f}%")
print(f"  {'Test Accuracy':<25} {test_acc*100:>9.2f}%")
print(f"  {'Test Loss':<25} {test_loss:>10.4f}")

# ── STEP 7: Training Curves ──────────────────────────────────
print(f"\n📈 STEP 7: Training Curves...")
ep = range(1, epochs_ran + 1)
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle(f'Fashion MNIST CNN – Training History  (Test Acc: {test_acc*100:.2f}%)',
             fontsize=13, fontweight='bold')

axes[0].plot(ep, history.history['accuracy'],     'b-o', markersize=4, label='Train')
axes[0].plot(ep, history.history['val_accuracy'], 'r-o', markersize=4, label='Validation')
axes[0].axhline(y=test_acc, color='green', linestyle='--', linewidth=1.5,
                label=f'Test={test_acc*100:.1f}%')
axes[0].set_title('Model Accuracy', fontweight='bold')
axes[0].set_xlabel('Epoch'); axes[0].set_ylabel('Accuracy')
axes[0].legend(); axes[0].grid(True, alpha=0.3)
axes[0].set_ylim([0, 1])

axes[1].plot(ep, history.history['loss'],     'b-o', markersize=4, label='Train')
axes[1].plot(ep, history.history['val_loss'], 'r-o', markersize=4, label='Validation')
axes[1].set_title('Model Loss', fontweight='bold')
axes[1].set_xlabel('Epoch'); axes[1].set_ylabel('Loss')
axes[1].legend(); axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('training_curves.png', dpi=150, bbox_inches='tight')
print("  ✅ Saved: training_curves.png")

# ── STEP 8: Predictions & Confusion Matrix ───────────────────
print(f"\n🔍 STEP 8: Predictions & Confusion Matrix...")
y_pred_probs = model.predict(X_test, verbose=0)
y_pred       = np.argmax(y_pred_probs, axis=1)

cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots(figsize=(11, 9))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=CLASS_NAMES, yticklabels=CLASS_NAMES,
            ax=ax, linewidths=0.3)
ax.set_title(f'Confusion Matrix  (Test Acc: {test_acc*100:.2f}%)',
             fontsize=13, fontweight='bold')
ax.set_xlabel('Predicted Label', fontsize=11)
ax.set_ylabel('True Label', fontsize=11)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=150, bbox_inches='tight')
print("  ✅ Saved: confusion_matrix.png")

print(f"\n  Classification Report:")
print(classification_report(y_test, y_pred, target_names=CLASS_NAMES))

# ── STEP 9: Correct & Incorrect Predictions ──────────────────
print(f"\n🖼️  STEP 9: Correct & Incorrect Predictions...")

correct_idx   = np.where(y_pred == y_test)[0]
incorrect_idx = np.where(y_pred != y_test)[0]

fig, axes = plt.subplots(4, 5, figsize=(15, 13))
fig.suptitle('CNN Predictions – Correct (green) vs Incorrect (red)',
             fontsize=13, fontweight='bold')

# Top 2 rows: 10 correct
for i, ax in enumerate(axes[:2].flat):
    idx  = correct_idx[i]
    img  = X_test[idx].squeeze()
    pred = CLASS_NAMES[y_pred[idx]]
    conf = y_pred_probs[idx][y_pred[idx]] * 100
    ax.imshow(img, cmap='gray')
    ax.set_title(f'✓ {pred}\n({conf:.0f}%)', fontsize=8, color='green')
    ax.axis('off')

# Bottom 2 rows: 10 incorrect
for i, ax in enumerate(axes[2:].flat):
    idx    = incorrect_idx[i]
    img    = X_test[idx].squeeze()
    pred   = CLASS_NAMES[y_pred[idx]]
    actual = CLASS_NAMES[y_test[idx]]
    conf   = y_pred_probs[idx][y_pred[idx]] * 100
    ax.imshow(img, cmap='gray')
    ax.set_title(f'✗ Pred:{pred}\nTrue:{actual} ({conf:.0f}%)',
                 fontsize=7.5, color='red')
    ax.axis('off')

plt.tight_layout()
plt.savefig('correct_vs_incorrect.png', dpi=150, bbox_inches='tight')
print("  ✅ Saved: correct_vs_incorrect.png")

# ── STEP 10: Console Predictions Table ───────────────────────
print(f"\n  Sample Predictions (first 15 test images):")
print(f"  {'#':<4} {'Actual':<16} {'Predicted':<16} {'Conf':>7} {'Result'}")
print(f"  {'-'*55}")
for i in range(15):
    a    = CLASS_NAMES[y_test[i]]
    p    = CLASS_NAMES[y_pred[i]]
    conf = y_pred_probs[i][y_pred[i]] * 100
    mark = "✅" if y_pred[i] == y_test[i] else "❌"
    print(f"  {i+1:<4} {a:<16} {p:<16} {conf:>6.1f}% {mark}")

total_correct = np.sum(y_pred == y_test)
print(f"\n  Total correct: {total_correct}/{len(y_test)}  ({total_correct/len(y_test)*100:.2f}%)")

print(f"\n{'=' * 64}")
print(f"  ✅  Fashion MNIST CNN Classifier Complete!")
print(f"  🎯  Final Test Accuracy : {test_acc*100:.2f}%")
print(f"{'=' * 64}")
