from django.http import JsonResponse

def map_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'map': None
        })

def map_post_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def map_put_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def map_delete_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })