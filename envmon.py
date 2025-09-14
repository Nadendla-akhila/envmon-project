import time
import random
import csv
from datetime import datetime

def simulate_sensor_data():
    """Simulates temperature and humidity readings."""
    temperature = round(random.uniform(20.0, 35.0), 2)  # °C
    humidity = round(random.uniform(30.0, 70.0), 2)     # %
    return temperature, humidity

def log_data_to_csv(temperature, humidity):
    """Logs the readings into a CSV file with timestamp."""
    with open("environment_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), temperature, humidity])

def main():
    print("🌱 EnvMon started... (Press Ctrl+C to stop)")
    print("Logging data into environment_log.csv\n")
    
    # Write CSV header once
    with open("environment_log.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)"])

    while True:
        temperature, humidity = simulate_sensor_data()
        print(f"🌡️ Temp: {temperature}°C | 💧 Humidity: {humidity}%")
        log_data_to_csv(temperature, humidity)
        time.sleep(5)  # wait 5 seconds

if __name__ == "__main__":
    main()
