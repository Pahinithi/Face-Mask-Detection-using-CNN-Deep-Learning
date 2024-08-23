# Face Mask Detection using CNN (Deep Learning)


## Overview

This project focuses on building a Face Mask Detection system using Convolutional Neural Networks (CNN) in deep learning. The system is designed to distinguish between images of people wearing masks and those not wearing masks. The model is trained on a dataset of images, and the web application is built using Flask.

## Table of Contents

- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Web Application](#web-application)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Structure

```
Face-Mask-Detection-using-CNN-Deep-Learning/
│
├── static/                 # Static files (CSS, images, etc.)
├── templates/              # HTML templates
│   ├── index.html          # Main page of the web application
├── model/                  # Trained model and related files
│   ├── Newmodelface.h5     # Trained model in HDF5 format
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── README.md               # Project README file
└── ...
```

## Dataset

The dataset used in this project consists of images of people with and without face masks. The images are split into training and testing sets to evaluate the model's performance.

- **With Mask**: 3,725 images
- **Without Mask**: 3,828 images

## Model Architecture

The model is built using TensorFlow/Keras and follows a simple CNN architecture:

- **Convolutional Layers**: To extract features from the images.
- **MaxPooling Layers**: To reduce the spatial dimensions.
- **Fully Connected Layers**: For the final classification.
- **Dropout Layers**: To prevent overfitting.

The final output layer uses a sigmoid activation function for binary classification.

## Web Application

A web application was developed using Flask to allow users to upload images and receive predictions on whether the person in the image is wearing a mask.

### UI/UX Design

The web interface is designed to be simple and user-friendly with a visually appealing layout. Users can upload an image, and the application will display the prediction along with a confidence score.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Pahinithi/Face-Mask-Detection-using-CNN-Deep-Learning.git
   cd Face-Mask-Detection-using-CNN-Deep-Learning
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

- Upload an image by clicking the upload button.
- The model will process the image and display whether the person is wearing a mask or not.
- The prediction result will be shown below the upload button with a confidence score.

## Screenshots

<img width="1728" alt="DL06" src="https://github.com/user-attachments/assets/08231a63-1e17-4830-a1a8-69f37e7963f8">


## Future Work

- **Model Improvements**: Experiment with different architectures or hyperparameters to improve accuracy.
- **Dataset Expansion**: Collect more diverse images to enhance model generalization.
- **Deployment**: Deploy the application to a cloud platform for broader accessibility.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for discussion.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The dataset used in this project was obtained from [Kaggle](https://www.kaggle.com/).

