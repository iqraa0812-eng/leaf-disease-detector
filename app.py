import json
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

CONFIDENCE_THRESHOLD = 0.80  # below this, the app says it is not sure

st.set_page_config(page_title="Leaf Disease Detector", page_icon="🌿")
st.title("🌿 Leaf Disease Detector")
st.caption("Best results: a close-up photo of ONE leaf on a plain background, in good light.")


@st.cache_resource
def load():
    model = tf.keras.models.load_model("leaf_model.keras")
    names = json.load(open("class_names.json"))
    info = json.load(open("disease_info.json", encoding="utf-8"))
    meta = json.load(open("model_info.json"))
    return model, names, info, meta


def pretty(label):
    return label.replace("___", " - ").replace("_", " ")


model, names, info, meta = load()

file = st.file_uploader("Upload a clear photo of one leaf", type=["jpg", "jpeg", "png"])
if file:
    img = Image.open(file).convert("RGB")
    st.image(img)
    x = np.expand_dims(np.array(img.resize((224, 224)), dtype="float32"), 0)
    probs = model.predict(x)[0]
    i = int(np.argmax(probs))

    # Not confident enough: do not name a disease, show the top guesses instead
    if probs[i] < CONFIDENCE_THRESHOLD:
        st.warning(
            f"Not sure about this photo (top guess confidence: {probs[i]:.0%}). "
            "Try a close-up of ONE leaf on a plain background in good light."
        )
        st.subheader("Top guesses")
        for j in np.argsort(probs)[::-1][:3]:
            st.write(f"{pretty(names[j])}: {probs[j]:.0%}")
        st.stop()

    label = names[i]
    crop, disease = label.split("___")
    crop = crop.replace("_", " ")
    disease = disease.replace("_", " ")
    d = info.get(label, {})

    st.header(f"1. Disease: {disease}")
    st.write(f"**2. Affected crop / plant:** {crop}")
    if disease.strip().lower() == "healthy":
        st.success("This leaf looks healthy.")
    else:
        st.subheader("3. Symptoms")
        st.write(d.get("symptoms", "Not added yet."))
        st.subheader("4. Disease type & cause")
        st.write(d.get("type_cause", "Not added yet."))
        st.subheader("5. Severity levels")
        for level, text in d.get("severity", {}).items():
            st.write(f"**{level}:** {text}")
        st.subheader("6. How it spreads")
        st.write(d.get("spread", "Not added yet."))
        st.subheader("7. Treatment & prevention")
        st.write(f"**Treatment:** {d.get('treatment', 'Not added yet.')}")
        st.write(f"**Prevention:** {d.get('prevention', 'Not added yet.')}")

    st.subheader("8. AI detection accuracy")
    st.write(f"**Confidence for this photo:** {probs[i]:.0%}")
    st.write(f"**Model's overall validation accuracy:** {meta['val_accuracy']}%")
    st.caption(
        "The validation accuracy comes from clean lab-style photos. "
        "Accuracy on real field photos with busy backgrounds can be lower."
    )
    with st.expander("Other possibilities"):
        for j in np.argsort(probs)[::-1][1:4]:
            st.write(f"{pretty(names[j])}: {probs[j]:.0%}")