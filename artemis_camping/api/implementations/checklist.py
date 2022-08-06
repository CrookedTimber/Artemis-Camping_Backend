from django.http import JsonResponse

def checklist_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'checklist': []
        })

def checklist_post_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def checklist_put_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })

def checklist_delete_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })