from django.http import JsonResponse

def member_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'member': None
        })

def member_post_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def member_put_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def member_delete_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })