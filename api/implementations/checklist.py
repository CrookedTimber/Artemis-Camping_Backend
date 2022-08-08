from django.http import JsonResponse

def checklist_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'checklist': [{
            'id':1,
            'item':'Prepare and bring the tents',
            'remark':'We booked a SUV',
            'user_in_charge':'Wing',
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Wing',
            'update_user':'Wing'
            },
            {
            'id':2,
            'item':'Prepare load of foods',
            'remark':'Prepare foods for 5 of us',
            'user_in_charge':'Sam',
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Wing',
            'update_user':'Wing'
            }]
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