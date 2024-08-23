from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

# Initialize Flask application
app = Flask(__name__, template_folder='templates')

# Load the trained model
model = load_model("Newmodelface.h5")

# Define image size
IMG_SIZE = (128, 128)

# Define the home route
@app.route("/")
def home():
    return render_template("index.html")

# Define the prediction route
@app.route("/predict", methods=["POST"])
def predict():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return render_template("index.html", prediction="No file uploaded.")

    file = request.files['file']
    
    # Check if the file is an image
    if file.filename == '':
        return render_template("index.html", prediction="No file selected.")
    
    if file:
        # Process the image
        image = Image.open(file)
        image = image.resize(IMG_SIZE)
        image = image.convert('RGB')
        image = np.array(image) / 255.0  # Normalize the image
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Make prediction
        prediction = model.predict(image)
        prediction_class = "Mask" if prediction[0][0] < 0.5 else "No Mask"

        # Return prediction to the template
        return render_template("index.html", prediction=f"The person is likely {prediction_class}.")

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
