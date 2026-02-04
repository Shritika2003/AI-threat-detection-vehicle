#  AI-Driven Threat Detection in Autonomous Vehicles

This project implements a real-time anomaly detection system using Machine Learning to detect potential cyber threats in autonomous vehicles. It uses synthetic sensor data (speed, ECU, throttle, brake) and applies the **Isolation Forest algorithm** to identify anomalies in vehicle behavior.

---

##  Features

- Simulates vehicle log data with normal and anomalous behavior
- Trains a lightweight Isolation Forest model
- Real-time cyber threat detection via **Streamlit GUI**
- Alerts and logs suspicious entries
- Beginner-friendly Python implementation
  

---
## How to Run the Application

Step 1: Open Terminal / Command Prompt
Navigate to the project directory:
cd your_project_directory

Step 2: Install Required Dependencies
pip install -r requirements.txt

Step 3: Run the Streamlit Application
streamlit run streamlit_app.py

Step 4: Open the Application in Browser
Open the following URL in your browser:
http://localhost:8501

Public IP Access (Remote Access)
Run the application using:
streamlit run streamlit_app.py --server.address 0.0.0.0 --server.port 8501



