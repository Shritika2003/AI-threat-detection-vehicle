
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

model = joblib.load("model.pkl")
df = pd.read_csv("vehicle_logs.csv")
df_raw = df.copy()
df = df.drop(columns=["timestamp"])
df["ecu"] = LabelEncoder().fit_transform(df["ecu"])

df_raw["anomaly"] = model.predict(df)
df_raw["anomaly"] = df_raw["anomaly"].map({1: "Normal", -1: "Anomaly"})
anomalies = df_raw[df_raw["anomaly"] == "Anomaly"]
print(anomalies)
