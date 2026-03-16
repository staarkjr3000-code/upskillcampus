"""
IoT Based Smart Monitoring System
Industrial Internship Project
Name: Soumeel Mallick
Domain: Internet of Things (IoT)
"""

import time
import random
from datetime import datetime


class Sensor:
    """
    Simulates environmental sensors
    """

    def read_temperature(self):
        return round(random.uniform(20, 35), 2)

    def read_humidity(self):
        return round(random.uniform(40, 80), 2)

    def read_air_quality(self):
        return round(random.uniform(100, 300), 2)


class CloudPlatform:
    """
    Simulates sending data to cloud
    """

    def send_data(self, data):
        print("\nSending data to cloud...")
        time.sleep(1)
        print("Data uploaded successfully!\n")
        print("Cloud Record:", data)


class IoTMonitoringSystem:
    """
    Main IoT Monitoring System
    """

    def __init__(self):
        self.sensor = Sensor()
        self.cloud = CloudPlatform()

    def collect_data(self):
        temperature = self.sensor.read_temperature()
        humidity = self.sensor.read_humidity()
        air_quality = self.sensor.read_air_quality()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data = {
            "timestamp": timestamp,
            "temperature": temperature,
            "humidity": humidity,
            "air_quality": air_quality
        }

        return data

    def display_data(self, data):
        print("\n---- IoT Sensor Data ----")
        print("Time:", data["timestamp"])
        print("Temperature:", data["temperature"], "°C")
        print("Humidity:", data["humidity"], "%")
        print("Air Quality Index:", data["air_quality"])
        print("-------------------------")

    def run(self):
        print("Starting IoT Smart Monitoring System...\n")

        for i in range(5):
            data = self.collect_data()
            self.display_data(data)
            self.cloud.send_data(data)

            time.sleep(2)

        print("\nMonitoring completed successfully.")


if __name__ == "__main__":
    system = IoTMonitoringSystem()
    system.run()
