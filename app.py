# app.py

import os
import tensorflow as tf
import numpy as np
from PIL import Image
from flask import Flask, request, render_template, url_for, send_from_directory

# --- 1. SETUP ---
# Initialize the Flask application
app = Flask(__name__)

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# --- 2. LOAD THE TRAINED MODEL AND CLASS NAMES ---
# Load the model once when the application starts
try:
    model = tf.keras.models.load_model('tomato_disease_recognizer_best.keras')
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# Load the class names
with open('class_names.txt', 'r') as f:
    class_names = [line.strip() for line in f.readlines()]
print(f"✅ Class names loaded: {class_names}")

# --- 3. UTILITY FUNCTIONS ---
def allowed_file(filename):
    """Checks if the file's extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path, target_size=(224, 224)):
    """Preprocesses the image for the model."""
    img = Image.open(image_path)
    # Ensure image is in RGB format
    if img.mode != "RGB":
        img = img.convert("RGB")
    img = img.resize(target_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) # Create a batch
    
    # Use the ResNetV2 preprocessing function
    processed_image = tf.keras.applications.resnet_v2.preprocess_input(img_array)
    return processed_image

# --- 4. FLASK ROUTES ---
@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles the main page and image upload."""
    if request.method == 'POST':
        # Check if a file was posted
        if 'file' not in request.files:
            return "No file part in the request.", 400
        
        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file
        if file.filename == '':
            return "No file selected.", 400

        if file and allowed_file(file.filename):
            # Save the uploaded file
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Preprocess the image and get a prediction
            processed_image = preprocess_image(filepath)
            predictions = model.predict(processed_image)
            
            # Get the top prediction
            predicted_class_index = np.argmax(predictions[0])
            predicted_class_name = class_names[predicted_class_index]
            confidence = np.max(predictions[0]) * 100

            # Render the result page
            return render_template('result.html', 
                                   prediction=predicted_class_name, 
                                   confidence=f"{confidence:.2f}",
                                   image_file=filename)
        else:
            return "Invalid file type.", 400

    # For a GET request, just show the upload page
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serves the uploaded image file to be displayed on the result page."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# --- 5. RUN THE APP ---
if __name__ == '__main__':
    # Create the upload directory if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # Run the app
    app.run(debug=True)