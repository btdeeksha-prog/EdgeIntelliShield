from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and encoder
model = pickle.load(open("fraud_model.pkl", "rb"))
encoder = pickle.load(open("label_encoder.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    step = int(request.form["step"])
    type_trans = request.form["type"]
    amount = float(request.form["amount"])
    oldbalanceOrg = float(request.form["oldbalanceOrg"])
    newbalanceOrig = float(request.form["newbalanceOrig"])
    oldbalanceDest = float(request.form["oldbalanceDest"])
    newbalanceDest = float(request.form["newbalanceDest"])

    # Encode type
    type_encoded = encoder.transform([type_trans])[0]

    features = np.array([[step, type_encoded, amount,
                          oldbalanceOrg, newbalanceOrig,
                          oldbalanceDest, newbalanceDest]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Fraud Transaction Detected"
    else:
        result = "Safe Transaction"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True, port=4040)