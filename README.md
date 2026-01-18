# Tomato Leaf Disease Detection

This project works on detecting tomato leaf diseases using a Deep Learning model (ResNet50V2) integrated into a Flask web application. Users can upload an image of a tomato leaf, and the system will predict the disease along with a confidence score.

## 📌 Features

-   **Deep Learning Model**: Uses a pre-trained ResNet50V2 model fine-tuned for tomato disease classification.
-   **User-Friendly Interface**: A simple web interface built with Flask for easy image uploading and prediction.
-   **Real-time Prediction**: Instantly classifies uploaded images into one of the known disease categories or healthy status.

## 🦠 Detectable Diseases

The model can identify the following 11 classes:

1.  Bacterial Spot
2.  Early Blight
3.  Late Blight
4.  Leaf Mold
5.  Septoria Leaf Spot
6.  Spider Mites (Two-spotted spider mite)
7.  Target Spot
8.  Tomato Yellow Leaf Curl Virus
9.  Tomato Mosaic Virus
10. Powdery Mildew
11. Healthy

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Kavi-ya/Tomato-leaf-disease-detection.git
    cd Tomato-leaf-disease-detection
    ```

2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  **Open your browser:**
    Go to `http://127.0.0.1:5000/`.

3.  **Upload an Image:**
    Click on the prompt to select a tomato leaf image and view the prediction result.

## 📁 Project Structure

-   `Models/`: Directory for storing model files.
-   `static/`: Contains static assets (CSS, images, uploads).
-   `templates/`: HTML templates for the Flask app.
-   `app.py`: Main Flask application script.
-   `class_names.txt`: List of disease classes.
-   `tomato_disease_recognizer_best.keras`: The trained Keras model.
-   `requirements.txt`: Python dependencies.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).