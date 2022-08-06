from django.http import JsonResponse

def budget_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'budget': []
        })

def budget_post_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def budget_put_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def budget_delete_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })