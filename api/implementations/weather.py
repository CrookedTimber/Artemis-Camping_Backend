from api.outgoing_api.weather_api import *

def weather_get_handler(request, parameters):
    array = parameters.split('&')
    json = get_weather('weather', array)
    return JsonResponse(json)