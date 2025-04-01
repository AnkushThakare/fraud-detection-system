import joblib
import numpy as np
import streamlit as st
from data_preprocessing import load_and_preprocess_data


def load_model():
    return joblib.load("fraud_detection_model.pkl")


# Streamlit Web App
st.title("Credit Card Fraud Detection")
st.write("Enter transaction details below to predict fraud:")

# Example input fields (adjust based on dataset features)
feature_inputs = []
for i in range(30):  # Assuming 30 features
    feature_inputs.append(st.number_input(f"Feature {i + 1}", value=0.0))

if st.button("Predict Fraud"):
    model = load_model()
    input_data = np.array(feature_inputs).reshape(1, -1)
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Legitimate.")
