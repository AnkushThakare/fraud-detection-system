from flask import Flask, request, jsonify
import joblib
import time

app = Flask(__name__)


# Load the trained model
model = joblib.load("fraud_detection_model.pkl")

# Store the last transaction per user
user_transactions = {}  # Dictionary to track {user_id: {"amount": X, "time": Y}}

@app.route("/predict", methods=["POST"])
def predict():
    global user_transactions

    data = request.get_json()
    features = data["features"]
    user_id = data["user_id"]  # User-specific identifier (e.g., account ID)

    transaction_amount = features[0]  # First feature (assuming it's the amount)
    timestamp = time.time()  # Get current time

    # Check if the user has made a recent transaction with the same amount
    if user_id in user_transactions:
        last_amount = user_transactions[user_id]["amount"]
        last_time = user_transactions[user_id]["time"]
        time_diff = timestamp - last_time

        if last_amount == transaction_amount and time_diff < 10:  # Fraud if repeated within 10 sec
            return jsonify({
                "prediction": 1,
                "reason": f"User {user_id} repeated transaction of {transaction_amount} within {time_diff:.2f} sec."
            })

    # Predict using the model
    prediction = model.predict([features])[0]

    # Store the current transaction for this user
    user_transactions[user_id] = {"amount": transaction_amount, "time": timestamp}

    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
