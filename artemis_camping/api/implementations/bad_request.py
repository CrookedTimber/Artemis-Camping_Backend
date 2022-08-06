from django.http import JsonResponse

def bad_request():
    return JsonResponse(
        {'status':'FAIL',
        'message':'Bad Request'
        })