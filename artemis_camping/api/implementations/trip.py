from django.http import JsonResponse

def trip_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'trip': {
            'id':1,
            'name':'Peak District Trip',
            'public':False,
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Edgar',
            'update_user':'Edgar'
            }
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
