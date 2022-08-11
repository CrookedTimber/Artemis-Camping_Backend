from django.shortcuts import render
from django.http import HttpResponse

from api.implementations.bad_request import *
from api.implementations.budget import *
from api.implementations.checklist import *


from api.implementations.forecast import *
from api.implementations.home import *
from api.implementations.itinerary  import *
from api.implementations.landing import *
from api.implementations.login import *
from api.implementations.logout import *
from api.implementations.member import *
from api.implementations.messaging import *
from api.implementations.settings import *
from api.implementations.trip import *
from api.implementations.weather import *



from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    return HttpResponse("<h1>Artemis Camping API</h1>")

def tests(request):
    response = render(request, "tests.html")  # djang    http.    HttpResponse
    response.set_cookie(key='id', value=1)
    return response


def login_handler(request):
    if request.method == 'POST':
        return login_post_handler(request)
    return bad_request()

def logout_handler(request):
    if request.method == 'POST':
        return logout_post_handler(request)
    return bad_request()

#@login_required
@csrf_exempt
def budget_handler(request, trip_id):
    if request.method == 'GET':
        return budget_get_handler(request, trip_id)
    elif request.method == 'POST':
        return budget_post_handler(request, trip_id)
    elif request.method == 'PUT':
        return budget_put_handler(request, trip_id)
    elif request.method == 'DELETE':
        return budget_delete_handler(request, trip_id)
    return bad_request()

#@login_required
@csrf_exempt
def checklist_handler(request, trip_id):
    if request.method == 'GET':
        return checklist_get_handler(request, trip_id)
    elif request.method == 'POST':
        return checklist_post_handler(request, trip_id)
    elif request.method == 'PUT':
        return checklist_put_handler(request, trip_id)
    elif request.method == 'DELETE':
        return checklist_delete_handler(request, trip_id)
    return bad_request()

#@login_required

@csrf_exempt
def trip_handler(request):
    if request.method == 'GET':
        return trip_get_handler(request)
    elif request.method == 'POST':
        return trip_post_handler(request)
    return bad_request()

@csrf_exempt
def single_trip_handler(request, trip_id):
    if request.method == 'GET':
        return single_trip_get(request, trip_id)
    elif request.method == 'PUT':
        return single_trip_put(request, trip_id)
    elif request.method == 'DELETE':
        return single_trip_delete(request, trip_id)
    return bad_request()


#@login_required
def home_handler(request):
    if request.method == 'GET':
        return home_get_handler(request)
    return bad_request()

# @login_required
def itinerary_handler(request):
    if request.method == 'GET':
        return itinerary_get_handler(request)
    return bad_request()

#@login_required
def landing_handler(request):
    if request.method == 'GET':
        return landing_get_handler(request)
    return bad_request()


#@login_required
@csrf_exempt
def trip_members_handler(request, trip_id):
    if request.method == 'GET':
        return get_trip_members(request, trip_id)
    elif request.method == 'POST':
        return member_post_handler(request, trip_id)
    elif request.method == 'DELETE':
        return member_delete_handler(request, trip_id)
    elif request.method == 'PUT':
        return member_put_handler(request, trip_id)
    
    
    return bad_request()
        

@csrf_exempt
def messaging_handler(request, trip_id):
    if request.method == 'GET':
        return get_trip_messages(request, trip_id)
    elif request.method == 'POST':
        return messaging_post_handler(request, trip_id)
    elif request.method == 'DELETE':
        return message_delete_handler(request, trip_id)
    
    return bad_request()

#@login_required
def settings_handler(request):
    if request.method == 'GET':
        return settings_get_handler(request)
    elif request.method == 'PUT':
        return settings_put_handler(request)
    return bad_request()

#@login_required
def forecast_handler(request, parameters):
    if request.method == 'GET':
        return forecast_get_handler(request, parameters)
    return bad_request()


#@login_required
def weather_handler(request, parameters):
    if request.method == 'GET':
        return weather_get_handler(request, parameters)
    return bad_request()

