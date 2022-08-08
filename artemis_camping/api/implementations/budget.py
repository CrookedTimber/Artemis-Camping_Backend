from django.http import JsonResponse

def budget_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'budget': [{
            'id':1,
            'item':'Rental Car',
            'price':150,
            'remark':'We booked a SUV',
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Edgar',
            'update_user':'Edgar'
            },
            {
            'id':2,
            'item':'Base Camp',
            'price':350,
            'remark':'2 double rooms in base camp',
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Wing',
            'update_user':'Wing'
            }]
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