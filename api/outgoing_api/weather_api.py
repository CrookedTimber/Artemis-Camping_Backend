from django.http import JsonResponse
import requests
from dotenv import load_dotenv
import os
load_dotenv()
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

def get_weather(request_type, parameters):
    try:
        for cur in parameters:
            if cur.split('=')[0] == 'lat':
                lat = cur.split('=')[1]
            elif cur.split('=')[0] == 'long':
                long = cur.split('=')[1]
        url = 'https://api.openweathermap.org/data/2.5/' + request_type + '?lat=' + lat + '&lon=' + long + '&units=metric&APPID=' + WEATHER_API_KEY
        print(url)
        res = requests.get(url)
        return res.json()
    except:
        return None
