# 🌿 PiPlant AI – Smart Plant Monitoring and Auto-Watering System (Raspberry Pi 5)

**PiPlant AI** is an intelligent plant care system built for Raspberry Pi 5 that monitors soil moisture, light intensity, and temperature using sensors. It automates plant care by triggering a water pump when the soil is too dry. An optional camera module captures daily plant growth snapshots, and a Flask dashboard displays sensor data in real time. This project is perfect for home gardeners, biology students, and DIY smart farming enthusiasts.

## 🧰 Requirements

- Raspberry Pi 5 (with RPi.GPIO support)
- Soil moisture sensor (analog or digital)
- DHT11/DHT22 temperature + humidity sensor
- LDR for light sensing (optional)
- Relay module + water pump for irrigation
- PiCamera (optional)
- Flask, matplotlib, threading, etc.

## 🚀 Features

- Live dashboard with real-time sensor readings
- Automated watering when soil is dry
- Daily photo timelapse capture
- Historical data graphing (temp/humidity/moisture)
- Safe GPIO handling and threaded updates

## ▶️ How to Run

1. Wire your sensors to the Pi GPIO headers.
2. Install dependencies:

```bash
pip install flask matplotlib RPi.GPIO adafruit-circuitpython-dht
sudo apt-get install libgpiod2
```

3. Run the app:

```bash
python3 piplant_ai.py
```

4. Open in browser: `http://<raspberry-pi-ip>:5002/`

## 📷 Optional

Connect a PiCamera to enable plant timelapse snapshots, stored in the `snapshots/` directory.

---

Happy planting! 🌱