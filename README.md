# Project Description:
This project demonstrates the integration of an MQTT messaging system with the Gemini LLM API. The system includes:
- A Publisher (publisher.py) that simulates sensor data and publishes it to an MQTT topic.
- A Subscriber (subscriber.py) that listens to the MQTT topic, receives the sensor data, and processes it using the Gemini LLM API (gemini.py).
- Gemini API Integration (gemini.py) for analyzing the received data and providing insights.
- This setup is ideal for applications involving real-time IoT data analysis and natural language interaction.

# Setup:
- Python 3.7 or higher, An MQTT broker (e.g., test.mosquitto.org), A Gemini API key pip installed on your system, pip install paho-mqtt

# Install:
- Clone the repository

```
git clone https://github.com/your-username/mqtt-gemini-integration.git
cd mqtt-gemini-integration
```

- Set up a python environment using Virtualenv

```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

- Install dependencies

```
pip install paho-mqtt python-dotenv google-generativeai
```

- Create a .env file in the project directory, replace your_gemini_api_key with your actual Gemini API key
```
echo "GEMINI_API_KEY=your_gemini_api_key" > .env
```

# Usage
- Run Publisher
```
python pub.py
```

### Example output: Published to mysensor2: temperature: 21.8, humidity: 42.8

- Run Subscriber
```
python sub.py
```

### Example output: Received message on topic mysensor2: "temperature: 21.8, humidity: 42.8"

### Insights: **Temperature:** 21.8°C is a mild temperature, pleasant for many.  It's not excessively hot or cold.  However, individual comfort levels vary. **Humidity:** 42.8% is a moderate humidity level.  It's not overly dry or humid.  Again, individual preferences and acclimatization play a role in comfort perception.  Levels below 30% might be considered dry by some, while levels above 60% can feel sticky or muggy.

# Test the Gemini API
```
python gemini.py
```

### Example output: MQTT is a lightweight protocol for IoT devices to communicate efficiently.
