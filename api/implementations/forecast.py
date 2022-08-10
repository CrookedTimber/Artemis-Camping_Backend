from api.outgoing_api.weather_api import *

def forecast_get_handler(request, parameters):
    array = parameters.split('&')
    json = get_weather('forecast', array)
    return JsonResponse(json)