import google.generativeai as genai
from dotenv import load_dotenv
import os

def send_request(text):
    load_dotenv()
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(text)
    print(response.text)

def test_gemini():
    output = send_request("Explain MQTT")
    print(output)

if __name__ == '__main__':
    test_gemini()
