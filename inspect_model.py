import json
import tensorflow as tf

# Load class names
with open("class_names.json", "r") as f:
    class_names = json.load(f)

print("TOTAL CLASSES:", len(class_names))

for i, name in enumerate(class_names):
    print(i, ":", name)

# Load trained model
model = tf.keras.models.load_model("leaf_model.keras")

print("\nMODEL INPUT:", model.input_shape)
print("MODEL OUTPUT:", model.output_shape)