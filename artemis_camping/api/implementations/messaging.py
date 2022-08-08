from django.http import JsonResponse

def messaging_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'messaging': [{
            'id':1,
            'message_body':'Lets go for Red route!',
            'create_date':'2022-08-08',
            'create_user':'Wing'
            },
            {
            'id':2,
            'message_body':'Are your crazy?',
            'create_date':'2022-08-08',
            'create_user':'Simon'
            },
            {
            'id':3,
            'message_body':'Love challenging route!',
            'create_date':'2022-08-08',
            'create_user':'Edgar'
            },
            {
            'id':4,
            'message_body':'......',
            'create_date':'2022-08-08',
            'create_user':'Summira'
            },]
        })

def messaging_post_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })