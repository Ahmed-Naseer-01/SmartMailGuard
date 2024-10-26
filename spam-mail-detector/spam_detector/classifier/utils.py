# classifier/utils.py
import joblib
import os
from django.conf import settings

# Load the model
model_path = os.path.join(settings.BASE_DIR, 'classifier/models/spam_classifier.pkl')
clf = joblib.load(model_path)

def detect_spam(email_text):
    prediction = clf.predict([email_text])
    return "This is a Spam Email!" if prediction == 1 else "This is a Ham Email!"
