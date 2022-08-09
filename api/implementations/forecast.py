from api.outgoing_api.weather_api import *

def forecast_get_handler(request):
    json = get_weather('forecast')
    return JsonResponse(json)