from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("tests/", views.tests),
    path("login/", views.login_handler, name="login"),
    path("logout/", views.logout_handler, name="logout"),
    #            "/api/trip/"
    # GET Request, gets all trips
    # POST Request, creates new trip with places and initial member
    # POST body: {"name":"name", "latitude": coordinate number, "longitude": coordinate number, "start_date": HTML calendar input, "end_date": HTML calendar input}"""
    path("trip/", views.trip_handler, name="trip"),
    # """  /api/trip/<int>
    # GET Request: Gets a single trip
    # DELETE Request: Deletes a single trip  """
    path("trip/<int:trip_id>/", views.single_trip_handler, name="single_trip"),
    # api/trip/<int:trip_id>/members/
    # GET: get all trip members.
    # POST: Add a new member to a trip. Body: {"user_id": 1}
    # DELETE: Deletes a member from the trip. Body: {"user_id": 1}
    path(
        "trip/<int:trip_id>/members/", views.trip_members_handler, name="trip_members"
    ),
    # "api/trip/<int:trip_id>/messages/"
    # GET: get all trip messages.
    # POST: Add a new message to a trip. Body: {"message": "Hello"}
    # DELETE: Deletes a message from the trip. Body: {"message_id": 3}
    path("trip/<int:trip_id>/messages/", views.messaging_handler, name="trip_messages"),
    
     # "api/trip/<int:trip_id>/checklist/"
    # GET: get all trip checklist items.
    # POST: Add a new chacklist item to a trip. Body: {"item": "bring food", "remark": "we need food"}
    # DELETE: Deletes a checklist item from the trip. Body: {"item_id": 3}
    path(
        "trip/<int:trip_id>/checklist/", views.checklist_handler, name="trip_checklist"
    ),
    
      # "api/trip/<int:trip_id>/budget/"
    # GET: get all trip budget items.
    # POST: Add a new budget item to a trip. Body: {"item": "bring food", "remark": "we need food"}
    # DELETE: Deletes a budget item from the trip. Body: {"item_id": 3}
    
    path("trip/<int:trip_id>/budget/", views.budget_handler, name="trip_budget"),

    path("member/all/", views.all_member_handler, name="all_member"),

    path("home/", views.home_handler, name="home"),
    path("itinerary/", views.itinerary_handler, name="itinerary"),
    path("landing/", views.landing_handler, name="landing"),
    path("settings/", views.settings_handler, name="settings"),
    path("forecast/<parameters>", views.forecast_handler, name="forecast"),
    path("weather/<parameters>", views.weather_handler, name="weather"),
]
