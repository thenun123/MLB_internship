# ============================================================
#   Practice 1: Transfer Learning with MobileNetV2
#   - Load pre-trained model
#   - Explore architecture
#   - Freeze base layers
#   - Add custom classification head
# ============================================================

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.applications import MobileNetV2

print("=" * 60)
print("   TRANSFER LEARNING – MobileNetV2 EXPLORATION")
print("=" * 60)

# ── STEP 1: Load Pre-trained MobileNetV2 ─────────────────────
base_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

print(f"  ✅ MobileNetV2 loaded")
print(f"  Output shape : {base_model.output_shape}")
print(f"  Total layers : {len(base_model.layers)}")
print(f"  Parameters   : {base_model.count_params():,}")

# ── STEP 2: Explore Architecture ─────────────────────────────
print(f"\n🔍 First 10 layers:")
print(f"  {'Layer Name':<35} {'Type':<25} {'Output Shape'}")
print(f"  {'-'*75}")
for layer in base_model.layers[:10]:
    print(f"  {layer.name:<35} {type(layer).__name__:<25} {str(layer.output_shape)}")
print(f"  ... ({len(base_model.layers) - 10} more layers)")

print(f"\n📌 Last 5 layers:")
for layer in base_model.layers[-5:]:
    print(f"  {layer.name:<35} {type(layer).__name__:<25} {str(layer.output_shape)}")

# ── STEP 3: Freeze Base Model ─────────────────────────────────
base_model.trainable = False
print(f"\n🔒 Base model frozen.")
print(f"  Non-trainable layers : {sum(1 for l in base_model.layers if not l.trainable)}")

# ── STEP 4: Add Custom Classification Head ────────────────────
inputs  = tf.keras.Input(shape=(224, 224, 3))
x       = base_model(inputs, training=False)
x       = GlobalAveragePooling2D()(x)
x       = Dense(256, activation='relu')(x)
x       = Dropout(0.4)(x)
outputs = Dense(1, activation='sigmoid')(x)

model = Model(inputs, outputs, name="MobileNetV2_Transfer")
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

total_p     = model.count_params()
trainable_p = sum(tf.size(v).numpy() for v in model.trainable_variables)
print(f"\n  Total Parameters  : {total_p:,}")
print(f"  Trainable (head)  : {trainable_p:,}  ({trainable_p/total_p*100:.1f}%)")
print(f"  Frozen (base)     : {total_p-trainable_p:,}  ({(total_p-trainable_p)/total_p*100:.1f}%)")
