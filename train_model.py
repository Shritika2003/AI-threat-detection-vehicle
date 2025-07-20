
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("vehicle_logs.csv")
df = df.drop(columns=["timestamp"])
df["ecu"] = LabelEncoder().fit_transform(df["ecu"])

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df)

joblib.dump(model, "model.pkl")
print("Model trained and saved as model.pkl")
