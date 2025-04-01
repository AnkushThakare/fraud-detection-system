import joblib
import numpy as np

# Load the trained model
model = joblib.load("fraud_detection_model.pkl")

# Load the training data to check feature count
from data_preprocessing import load_and_preprocess_data
_, X_test, _, _ = load_and_preprocess_data()
expected_features = X_test.shape[1]  # Get the correct feature count

# Create a sample data point with the correct number of features
sample_data = np.random.rand(1, expected_features)  # Generate a random test sample

# Make prediction
prediction = model.predict(sample_data)
print("Prediction:", prediction)
