from api.outgoing_api.weather_api import *

def weather_get_handler(request):
    json = get_weather('weather')
    return JsonResponse(json)