# 🌿 Leaf Disease Detector

An AI-powered web application that identifies plant leaf diseases from uploaded images and provides easy-to-understand information about symptoms, causes, severity, treatment, and prevention.

Developed as a university project using **Python, TensorFlow, MobileNetV2, and Streamlit**, the application aims to make basic plant disease identification more accessible to students, gardeners, and farmers.

## ✨ Features

The application analyzes an uploaded leaf image and provides:

- **Disease Identification:** Predicts the most likely disease affecting the leaf.
- **Plant Identification:** Displays the associated crop or plant species.
- **Symptoms:** Explains the common signs of the detected disease.
- **Cause and Disease Type:** Provides information about the nature and possible causes of the disease.
- **Severity Information:** Displays general severity descriptions (mild, moderate, or severe).
- **Disease Spread:** Explains how the disease can spread between plants.
- **Treatment Recommendations:** Provides general treatment and management guidance.
- **Prevention Tips:** Suggests ways to reduce the risk of disease.
- **Prediction Confidence:** Displays the model's confidence in its prediction, alongside its overall validation accuracy.

The application also includes a low-confidence response to help avoid presenting uncertain predictions as reliable diagnoses.

## 🧠 Technology and Model

The disease classification model is built using **MobileNetV2**, a convolutional neural network architecture based on transfer learning.

The model uses ImageNet-pretrained weights with a custom classification head designed to recognize 38 plant disease and healthy-leaf categories.

**Model details:**

| Component           | Details             |
| ------------------- | ------------------- |
| Architecture        | MobileNetV2         |
| Learning approach   | Transfer Learning   |
| Framework           | TensorFlow / Keras  |
| Input image size    | 224 × 224 pixels    |
| Output categories   | 38                  |
| Crops covered       | 14                  |
| Validation accuracy | Approximately 95.3% |

## 📊 Dataset

The model was trained using the **New Plant Diseases Dataset (Augmented)**, based on the PlantVillage dataset and accessed through Kaggle.

The training dataset contains approximately:

- 70,295 training images
- 17,572 validation images
- 38 disease and healthy-leaf categories
- 14 crop types

The images were resized to 224 × 224 pixels for model training. Data augmentation techniques, including random flipping and rotation, were used to improve the model's ability to generalize.

## 🌱 Supported Crops

The model supports the following 14 crop types:

1. Apple
2. Blueberry
3. Cherry
4. Corn
5. Grape
6. Orange
7. Peach
8. Bell Pepper
9. Potato
10. Raspberry
11. Soybean
12. Squash
13. Strawberry
14. Tomato

Each crop has one or more supported disease or healthy-leaf categories.

## 🛠️ Technologies Used

- **Python** – Main programming language
- **TensorFlow and Keras** – Model development and image classification
- **MobileNetV2** – Pretrained deep learning architecture
- **Streamlit** – Interactive web application
- **Pillow (PIL)** – Image processing
- **NumPy** – Numerical operations and prediction processing

## 🚀 Installation and Setup

Follow these steps to run the application locally.

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd Leaf-Detector
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
Leaf-Detector/
│
├── app.py
├── leaf_model.keras
├── class_names.json
├── model_info.json
├── disease_info.json
├── requirements.txt
└── README.md
```

## ⚠️ Limitations

Although the model achieved approximately 95.3% validation accuracy on the dataset, this result should not be interpreted as equivalent accuracy on real-world photographs.

Some important limitations include:

- **Background Sensitivity:** The original training images generally contain isolated leaves with relatively simple backgrounds. Real garden and field photographs may produce less reliable predictions.
- **Limited Categories:** The model recognizes only its 38 trained categories. It cannot reliably identify unsupported plant species, diseases, or nutrient deficiencies.
- **Severity Estimation:** Severity descriptions are general information associated with a disease. The model does not measure the actual damage or severity on an individual leaf.
- **General Treatment Guidance:** Treatment recommendations are informational and should be verified with a qualified agricultural professional before application.
- **Prediction Confidence:** A high confidence score does not guarantee that a prediction is correct, particularly for unfamiliar images.

This project is intended as an educational and informational tool, not a replacement for professional agricultural diagnosis.

## 🔮 Future Improvements

Planned areas for further development include:

- Improving predictions on real-world field photographs.
- Expanding the training dataset with diverse images and natural backgrounds.
- Improving plant species and disease classification.
- Evaluating model performance on independent real-world datasets.
- Improving prediction reliability and uncertainty handling.
- Expanding the range of supported crops and diseases.

## 🙏 Acknowledgements

Special thanks to the contributors of the **PlantVillage dataset** (Hughes and Salathé, 2015) and the **New Plant Diseases Dataset (Augmented)** by Samir Bhattarai on Kaggle for providing the images used in developing this project.

---

**Developed as a university project using machine learning and web application technologies.**
