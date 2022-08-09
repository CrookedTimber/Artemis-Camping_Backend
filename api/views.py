# from django.shortcuts import render
from django.http import HttpResponse
from api.implementations.bad_request import *
from api.implementations.budget import *
from api.implementations.checklist import *
from api.implementations.duration import *
from api.implementations.forecast import *
from api.implementations.home import *
from api.implementations.itinerary  import *
from api.implementations.landing import *
from api.implementations.login import *
from api.implementations.logout import *
from api.implementations.map import *
from api.implementations.member import *
from api.implementations.messaging import *
from api.implementations.settings import *
from api.implementations.trip import *
from api.implementations.weather import *

# Create your views here.

def home(request):
    return HttpResponse("<h1>Artemis Camping API</h1>")

def simple_view(request):
    return HttpResponse("<h1>Test View</h1>")

def simple_view2(request):
    return HttpResponse("<h1>Second Test View</h1>")


def login_handler(request):
    if request.method == 'POST':
        return login_post_handler(request)
    return bad_request()

def logout_handler(request):
    if request.method == 'POST':
        return logout_post_handler(request)
    return bad_request()

#@login_required
def budget_handler(request):
    if request.method == 'GET':
        return budget_get_handler(request)
    elif request.method == 'POST':
        return budget_post_handler(request)
    elif request.method == 'PUT':
        return budget_put_handler(request)
    elif request.method == 'DELETE':
        return budget_delete_handler(request)
    return bad_request()

#@login_required
def checklist_handler(request):
    if request.method == 'GET':
        return checklist_get_handler(request)
    elif request.method == 'POST':
        return checklist_post_handler(request)
    elif request.method == 'PUT':
        return checklist_put_handler(request)
    elif request.method == 'DELETE':
        return checklist_delete_handler(request)
    return bad_request()

#@login_required
def trip_handler(request):
    if request.method == 'GET':
        return trip_get_handler(request)
    elif request.method == 'POST':
        return trip_post_handler(request)
    elif request.method == 'PUT':
        return trip_put_handler(request)
    elif request.method == 'DELETE':
        return trip_delete_handler(request)
    return bad_request()

#@login_required
def duration_handler(request):
    if request.method == 'GET':
        return duration_get_handler(request)
    elif request.method == 'POST':
        return duration_post_handler(request)
    elif request.method == 'PUT':
        return duration_put_handler(request)
    elif request.method == 'DELETE':
        return duration_delete_handler(request)
    return bad_request()

#@login_required
def home_handler(request):
    if request.method == 'GET':
        return home_get_handler(request)
    return bad_request()

#@login_required
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
def map_handler(request):
    if request.method == 'GET':
        return map_get_handler(request)
    elif request.method == 'POST':
        return map_post_handler(request)
    elif request.method == 'PUT':
        return map_put_handler(request)
    elif request.method == 'DELETE':
        return map_delete_handler(request)
    return bad_request()

#@login_required
def member_handler(request):
    if request.method == 'GET':
        return member_get_handler(request)
    elif request.method == 'POST':
        return member_post_handler(request)
    elif request.method == 'PUT':
        return member_put_handler(request)
    elif request.method == 'DELETE':
        return member_delete_handler(request)
    return bad_request()

#@login_required
def messaging_handler(request):
    if request.method == 'GET':
        return messaging_get_handler(request)
    elif request.method == 'POST':
        return messaging_post_handler(request)
    return bad_request()

#@login_required
def settings_handler(request):
    if request.method == 'GET':
        return settings_get_handler(request)
    elif request.method == 'PUT':
        return settings_put_handler(request)
    return bad_request()

#@login_required
def forecast_handler(request):
    if request.method == 'GET':
        return forecast_get_handler(request)
    return bad_request()

#@login_required
def weather_handler(request):
    if request.method == 'GET':
        return weather_get_handler(request)
    return bad_request()
