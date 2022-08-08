from django.http import JsonResponse

def weather_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'weathers': []
        })