
import json
import numpy as np
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model("leaf_model.keras")

# Load class names
with open("class_names.json", "r") as f:
    class_names = json.load(f)

print("\n========== MODEL INFORMATION ==========")

print("Input shape:", model.input_shape)
print("Output shape:", model.output_shape)
print("Number of classes:", len(class_names))

print("\n========== CLASS NAMES ==========")

for i, name in enumerate(class_names):
    print(i, ":", name)

print("\n========== MODEL LAYERS ==========")

for layer in model.layers:
    print(layer.name, layer.output.shape if hasattr(layer, "output") else "")

print("\n========== CHECK COMPLETE ==========")

print("HELLO! PYTHON IS WORKING")