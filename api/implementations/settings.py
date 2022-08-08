from django.http import JsonResponse

def settings_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'settings': []
        })

def settings_put_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })