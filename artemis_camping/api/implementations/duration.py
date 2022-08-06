from django.http import JsonResponse

def duration_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'duration': None
        })

def duration_post_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def duration_put_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def duration_delete_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })