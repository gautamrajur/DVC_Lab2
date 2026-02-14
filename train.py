# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import json
import os

# Load data
df = pd.read_csv("data/CC_GENERAL.csv")
df = df.dropna()
df = df.drop(columns=["CUST_ID"])

# Simple binary target: high vs low balance
df["TARGET"] = (df["BALANCE"] > df["BALANCE"].median()).astype(int)
X = df.drop(columns=["TARGET"])
y = df["TARGET"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
os.makedirs("models", exist_ok=True)
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save metrics
accuracy = model.score(X_test, y_test)
with open("metrics.json", "w") as f:
    json.dump({"accuracy": accuracy}, f)

print(f"Model saved. Accuracy: {accuracy:.4f}")