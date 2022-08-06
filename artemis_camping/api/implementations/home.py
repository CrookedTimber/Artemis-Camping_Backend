from django.http import JsonResponse

def home_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'home': None
        })