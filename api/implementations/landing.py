from django.http import JsonResponse

def landing_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'landing': None
        })