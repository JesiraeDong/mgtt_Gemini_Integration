# subscriber.py
import paho.mqtt.client as mqtt
import time

from gemini import send_request

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to broker")
        # Subscribe to topic
        client.subscribe("mysensor2")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

    payload = msg.payload.decode()
    prompt = f"Analyze this sensor data and provide insights: {payload}"
    output = send_request(prompt)
    print (output)


# Create subscriber client
subscriber = mqtt.Client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# Connect to public broker
print("Connecting to broker...")
subscriber.connect("test.mosquitto.org", 1883, 60)

# Start the subscriber loop
subscriber.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping subscriber...")
    subscriber.loop_stop()
    subscriber.disconnect()
