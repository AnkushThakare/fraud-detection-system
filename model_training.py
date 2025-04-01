from sklearn.ensemble import RandomForestClassifier
import joblib
from data_preprocessing import load_and_preprocess_data
from sklearn.metrics import accuracy_score





def train_model():
    # Load preprocessed data
    X_train, X_test, y_train, y_test = load_and_preprocess_data()

    print("Training the Random Forest model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Model training completed!")

    # After training
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2%}")

    # Save the trained model
    joblib.dump(model, "fraud_detection_model.pkl")
    print("Model saved successfully!")

    return model, X_test, y_test


if __name__ == "__main__":
    train_model()
