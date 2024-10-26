# SmartMailGuard (Spam Email Detector)

## Overview
The Spam Email Detector is a web application built with Django that leverages machine learning to classify emails as either spam or ham. This project utilizes a trained classifier model saved using `joblib`, which predicts the category of the email based on user input. The application features a sleek, hacker-themed interface, making it both functional and visually engaging.

## Features
- **User-Friendly Interface:** An intuitive form for users to input email text and receive classification results.
- **Real-Time Classification:** Users can check if an email is spam or ham in real time using the trained machine learning model.
- **Responsive Design:** The application is styled for a professional look with a hacker aesthetic.
- **Color-Coded Results:** Spam emails are highlighted in red, while ham emails are displayed in green for easy identification.

## Technologies Used
- Django
- Scikit-learn
- Joblib
- HTML/CSS
- Bootstrap (for styling)

## Installation
To run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spam-email-detector.git
   cd spam-email-detector

2. Install the required packages:
   ```bash
   pip install -r requirements.txt

3. Run the development server:
   ```bash
   python manage.py runserver
4. Access the application in your web browser at
    ```bash
    http://127.0.0.1:8000/classifier/classify/
## Usage
- Enter the email text in the provided input field and click "Check Email."
- The application will display whether the email is classified as spam or ham.
Contributing
