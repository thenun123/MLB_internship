# ============================================================
#   Practice 1: Install & Verify TensorFlow / Keras
# ============================================================

import tensorflow as tf
from tensorflow import keras
import numpy as np

print("=" * 50)
print("    TENSORFLOW & KERAS – INSTALLATION CHECK")
print("=" * 50)

print(f"\n✅ TensorFlow Version : {tf.__version__}")
print(f"✅ Keras Version      : {keras.__version__}")
print(f"✅ NumPy Version      : {np.__version__}")

# Check GPU availability
gpus = tf.config.list_physical_devices('GPU')
print(f"\n🖥️  GPU Available : {'Yes – ' + str(len(gpus)) + ' GPU(s) found' if gpus else 'No (using CPU)'}")

# Quick sanity check – tensor operation
a = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
b = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)
c = tf.matmul(a, b)

print(f"\n🔢 Quick Tensor Test (Matrix Multiply):")
print(f"   A = {a.numpy().tolist()}")
print(f"   B = {b.numpy().tolist()}")
print(f"   A × B = {c.numpy().tolist()}")

print(f"\n✅ TensorFlow is installed and working correctly!")
print("=" * 50)
