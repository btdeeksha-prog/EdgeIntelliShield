import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("fraud.csv")

# Encode transaction type
le = LabelEncoder()
df["type"] = le.fit_transform(df["type"])

# Features
X = df[[
    "step",
    "type",
    "amount",
    "oldbalanceOrg",
    "newbalanceOrig",
    "oldbalanceDest",
    "newbalanceDest"
]]

# Target
y = df["isFraud"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=50)

# Train
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("fraud_model.pkl", "wb"))

# Save encoder
pickle.dump(le, open("label_encoder.pkl", "wb"))

print("Model Trained Successfully")