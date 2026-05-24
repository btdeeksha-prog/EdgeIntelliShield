import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("dataset/fraud.csv")

# Remove unnecessary columns
df = df.drop(["nameOrig", "nameDest"], axis=1)

# Encode transaction type
encoder = LabelEncoder()

df["type"] = encoder.fit_transform(df["type"])

# Features
X = df.drop("isFraud", axis=1)

# Target
y = df["isFraud"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestClassifier(
    n_estimators=50,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Save model
pickle.dump(model, open("models/fraud_model.pkl", "wb"))

# Save encoder
pickle.dump(encoder, open("models/label_encoder.pkl", "wb"))

print("Pickle files saved successfully")