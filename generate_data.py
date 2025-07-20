
import pandas as pd
import numpy as np

np.random.seed(42)

def generate_data(filename="vehicle_logs.csv"):
    data = []
    for i in range(500):
        if i < 475:
            speed = np.random.normal(60, 10)
            gps_lat = np.random.normal(28.61, 0.005)
            gps_lon = np.random.normal(77.23, 0.005)
            brake_pressure = np.random.uniform(0.1, 0.4)
            throttle = np.random.uniform(0.2, 0.6)
            ecu = "engine"
        else:
            speed = np.random.choice([0, 150, 200])
            gps_lat = np.random.uniform(25, 35)
            gps_lon = np.random.uniform(70, 80)
            brake_pressure = np.random.uniform(0, 1)
            throttle = np.random.uniform(0, 1)
            ecu = np.random.choice(["unknown", "brake", "transmission"])
        timestamp = pd.Timestamp("2024-01-01 10:00:00") + pd.Timedelta(seconds=i)
        data.append([timestamp, speed, gps_lat, gps_lon, brake_pressure, throttle, ecu])
    df = pd.DataFrame(data, columns=["timestamp", "speed", "gps_lat", "gps_lon", "brake_pressure", "throttle", "ecu"])
    df.to_csv(filename, index=False)

generate_data()
