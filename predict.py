import joblib
import pandas as pd

# Load model
model = joblib.load("fraud_detection_model.pkl")

# Load sample test data (modify as needed)
sample_data = pd.DataFrame([...])  # Replace with real test data

# Predict
predictions = model.predict(sample_data)
print(predictions)
