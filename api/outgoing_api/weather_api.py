from django.http import JsonResponse
import requests
from dotenv import load_dotenv
import os
load_dotenv()
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

def get_weather(request_type):
    try:
        url = 'https://api.openweathermap.org/data/2.5/' + request_type + '?q=London,uk&APPID=' + WEATHER_API_KEY
        print(url)
        res = requests.get(url)
        return res.json()
    except:
        return None
