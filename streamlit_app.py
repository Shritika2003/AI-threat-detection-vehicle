
import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

st.title("🚗 AI Threat Detection in Autonomous Vehicles")
st.markdown("Detect anomalies in vehicle sensor data using Isolation Forest")

uploaded_file = st.file_uploader("Upload vehicle_logs.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df_raw = df.copy()

    # Drop timestamp and encode
    if "timestamp" in df.columns:
        df = df.drop(columns=["timestamp"])

    if "ecu" in df.columns:
        le = LabelEncoder()
        df["ecu"] = le.fit_transform(df["ecu"])

    # Load model
    model = joblib.load("model.pkl")
    df_raw["anomaly"] = model.predict(df)
    df_raw["anomaly"] = df_raw["anomaly"].map({1: "✅ Normal", -1: "🚨 Anomaly"})

    st.subheader("📊 Anomaly Detection Result")
    st.write(df_raw[df_raw["anomaly"] == "🚨 Anomaly"])

    st.subheader("Summary")
    st.metric("Total Logs", len(df_raw))
    st.metric("Anomalies Found", (df_raw["anomaly"] == "🚨 Anomaly").sum())
