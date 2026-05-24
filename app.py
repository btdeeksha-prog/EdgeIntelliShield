from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("fraud_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    amount = float(request.form["amount"])
    location = int(request.form["location"])
    device = int(request.form["device"])

    features = np.array([[amount, location, device]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Fraud Transaction Detected"
    else:
        result = "Safe Transaction"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True, port=4040)