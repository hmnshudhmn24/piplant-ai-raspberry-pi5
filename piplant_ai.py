import time
import threading
import random
from flask import Flask, render_template_string

app = Flask(__name__)

# Simulate sensor data (replace with real GPIO sensor readings in practice)
sensor_data = {
    'moisture': 50,
    'temperature': 25.0,
    'humidity': 60,
    'light': 300,
    'auto_watered': False
}

def read_sensors():
    sensor_data['moisture'] = random.randint(30, 100)
    sensor_data['temperature'] = round(random.uniform(20.0, 30.0), 1)
    sensor_data['humidity'] = random.randint(40, 80)
    sensor_data['light'] = random.randint(100, 600)
    sensor_data['auto_watered'] = sensor_data['moisture'] < 40

def update_sensors_loop():
    while True:
        read_sensors()
        time.sleep(5)

@app.route('/')
def dashboard():
    return render_template_string("""
    <!doctype html>
    <html>
    <head><title>🌿 PiPlant AI Dashboard</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: sans-serif; padding: 20px; }
        .card { background: #eaffea; padding: 20px; border-radius: 10px; width: 300px; }
    </style>
    </head>
    <body>
        <div class="card">
        <h2>🌿 PiPlant AI</h2>
        <p><b>Soil Moisture:</b> {{data['moisture']}}%</p>
        <p><b>Temperature:</b> {{data['temperature']}}°C</p>
        <p><b>Humidity:</b> {{data['humidity']}}%</p>
        <p><b>Light Level:</b> {{data['light']}} Lux</p>
        <p><b>Status:</b>
        {% if data['auto_watered'] %}
            <span style='color:green;'>Watered</span>
        {% else %}
            <span style='color:red;'>Dry</span>
        {% endif %}
        </p>
        </div>
    </body>
    </html>
    """, data=sensor_data)

threading.Thread(target=update_sensors_loop, daemon=True).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)