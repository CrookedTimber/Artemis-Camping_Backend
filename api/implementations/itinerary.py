from django.http import JsonResponse

def itinerary_get_handler(request):
    return JsonResponse(
        {'status':'OK',
        'message':'',
        'itinerary': None
        })