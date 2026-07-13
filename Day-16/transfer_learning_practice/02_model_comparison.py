# ============================================================
#   Practice 2: Pre-trained Model Comparison
#   VGG16 vs ResNet50 vs MobileNetV2 vs EfficientNetB0
# ============================================================

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow.keras.applications import VGG16, ResNet50, MobileNetV2, EfficientNetB0

print("=" * 65)
print("   PRE-TRAINED MODEL COMPARISON – ImageNet Models")
print("=" * 65)

configs = [
    ("VGG16",          VGG16),
    ("ResNet50",       ResNet50),
    ("MobileNetV2",    MobileNetV2),
    ("EfficientNetB0", EfficientNetB0),
]

use_cases = {
    "VGG16"          : "Simple baseline, large memory, easy to understand",
    "ResNet50"       : "Deep networks, residual connections, great accuracy",
    "MobileNetV2"    : "Mobile/edge devices, lightweight, fast  ✅ Best for today",
    "EfficientNetB0" : "Best accuracy/efficiency ratio, latest architecture",
}

results = []
for name, ModelClass in configs:
    print(f"  Loading {name}...", end=" ", flush=True)
    m = ModelClass(input_shape=(224, 224, 3), include_top=False, weights=None)
    results.append((name, m.count_params(), len(m.layers)))
    print(f"✅  {m.count_params():>12,} params  {len(m.layers):>4} layers")

print(f"\n{'='*65}")
print(f"  {'Model':<18} {'Parameters':>14} {'Layers':>7}  Use Case")
print(f"  {'-'*63}")
for name, params, layers in results:
    print(f"  {name:<18} {params:>14,} {layers:>7}  {use_cases[name]}")

print(f"""
{'='*65}
🎯 Why MobileNetV2 for Cats vs Dogs:
   ✅ Only 2.3M parameters → trains faster
   ✅ 93–97% accuracy on binary classification
   ✅ Industry standard for transfer learning
   ✅ TFLite compatible → deployable to mobile
{'='*65}
""")
