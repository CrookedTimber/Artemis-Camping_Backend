from django.http import JsonResponse

def member_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'member': [{
            'id':1,
            'user_id':1,
            'user_name':'Wing',
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Edgar',
            'update_user':'Edgar'
            },
            {
            'id':2,
            'user_id':2,
            'user_name':'Edgar',
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Edgar',
            'update_user':'Edgar'
            },
            {
            'id':3,
            'user_id':3,
            'user_name':'Sam',
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Edgar',
            'update_user':'Edgar'
            },
            {
            'id':4,
            'user_id':4,
            'user_name':'Nathan',
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Edgar',
            'update_user':'Edgar'
            },
            {
            'id':5,
            'user_id':5,
            'user_name':'Summira',
            'create_date':'2022-08-08',
            'update_date':'2022-08-08',
            'create_user':'Edgar',
            'update_user':'Edgar'
            }]
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