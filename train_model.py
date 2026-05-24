import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Sample dataset
data = {
    "amount": [100, 5000, 200, 7000, 300],
    "location": [1, 0, 1, 0, 1],
    "device": [1, 0, 1, 0, 1],
    "fraud": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[["amount", "location", "device"]]
y = df["fraud"]

model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open("fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully")