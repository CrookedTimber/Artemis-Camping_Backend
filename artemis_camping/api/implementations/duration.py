from django.http import JsonResponse

def duration_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'duration': {
            'id':1,
            'start_date':'2022-08-15',
            'end_date':'2022-08-21',
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Wing',
            'update_user':'Wing'
            }
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