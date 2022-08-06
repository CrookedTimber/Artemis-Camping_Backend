from django.http import JsonResponse

def messaging_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'messaging': []
        })

def messaging_post_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })