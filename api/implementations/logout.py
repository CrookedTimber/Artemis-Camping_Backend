from django.http import JsonResponse

def logout_post_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':''
        })