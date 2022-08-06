from django.http import JsonResponse

def trip_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'trip': None
        })

def trip_post_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def trip_put_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def trip_delete_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })