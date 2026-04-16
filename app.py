import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

st.title("🚗 Vehicle Threat Detection System")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    df_raw = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Data")
    st.write(df_raw)

    # -------------------------------
    # 🔥 SMART COLUMN MAPPING
    # -------------------------------
    if "rpm" in df_raw.columns:
        df_raw["throttle"] = df_raw["rpm"]

    if "temperature" in df_raw.columns:
        df_raw["brake_pressure"] = df_raw["temperature"]

    # -------------------------------
    # ✅ REQUIRED COLUMNS
    # -------------------------------
    required_cols = ["speed", "gps_lat", "gps_lon", "brake_pressure", "throttle", "ecu"]

    # Create missing columns automatically
    for col in required_cols:
        if col not in df_raw.columns:
            df_raw[col] = 0

    # -------------------------------
    # 🎯 SELECT FEATURES
    # -------------------------------
    df = df_raw[required_cols].copy()

    # Encode ECU
    le = LabelEncoder()
    df["ecu"] = le.fit_transform(df["ecu"])

    # -------------------------------
    # 🤖 LOAD MODEL
    # -------------------------------
    model = joblib.load("model.pkl")

    # -------------------------------
    # 🔍 PREDICT
    # -------------------------------
    df_raw["anomaly"] = model.predict(df)

    # Convert output
    df_raw["anomaly"] = df_raw["anomaly"].map({1: "Normal", -1: "Anomaly"})

    # -------------------------------
    # 📊 SUMMARY
    # -------------------------------
    anomaly_count = (df_raw["anomaly"] == "Anomaly").sum()
    total = len(df_raw)
    status = "SAFE" if anomaly_count == 0 else "NOT SAFE"

    st.subheader("🚨 Summary")
    st.write(f"Total Data Points: {total}")
    st.write(f"Number of Anomalies Detected: {anomaly_count}")

    if status == "SAFE":
        st.success("Vehicle Status: SAFE ✅")
    else:
        st.error("Vehicle Status: NOT SAFE ⚠️")

    # -------------------------------
    # 📋 RESULTS TABLE
    # -------------------------------
    st.subheader("🔍 Detection Results")
    st.write(df_raw)

else:
    st.info("👆 Please upload a CSV file to start detection")
