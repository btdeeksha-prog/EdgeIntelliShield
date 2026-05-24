from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("models/fraud_model.pkl", "rb"))

# Load label encoder
encoder = pickle.load(open("models/label_encoder.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    step = int(request.form["step"])

    transaction_type = request.form["type"]

    amount = float(request.form["amount"])

    oldbalanceOrg = float(request.form["oldbalanceOrg"])

    newbalanceOrig = float(request.form["newbalanceOrig"])

    oldbalanceDest = float(request.form["oldbalanceDest"])

    newbalanceDest = float(request.form["newbalanceDest"])

    isFlaggedFraud = int(request.form["isFlaggedFraud"])

    # Encode type
    type_encoded = encoder.transform([transaction_type])[0]

    # Prepare features
    features = np.array([[
        step,
        type_encoded,
        amount,
        oldbalanceOrg,
        newbalanceOrig,
        oldbalanceDest,
        newbalanceDest,
        isFlaggedFraud
    ]])

    # Prediction
    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Fraud Transaction Detected"
    else:
        result = "Safe Transaction"

    return render_template(
        "index.html",
        prediction_text=result
    )

if __name__ == "__main__":
    app.run(debug=True, port=4040)