from django.http import JsonResponse

def login_post_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })