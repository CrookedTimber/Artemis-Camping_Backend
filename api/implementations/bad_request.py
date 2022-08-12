from django.http import JsonResponse

def bad_request():
    return JsonResponse(
        {'status':'400: FAIL',
        'message':'Bad Request'
        }, status=400)
