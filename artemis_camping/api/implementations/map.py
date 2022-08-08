from django.http import JsonResponse

def map_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'map': {
            'id':1,
            'location_from':'Point A',
            'location_to':'Point B',
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Edgar',
            'update_user':'Edgar'
            }
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