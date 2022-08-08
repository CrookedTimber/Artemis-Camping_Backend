from django.urls import path
from . import views
from .api_views import trip, api_test

urlpatterns = [
    path("", views.home),
    path("view/", views.simple_view, name="view"),
    path("view2/", views.simple_view2, name="vista"),
    
    
    path('trips-all/', trip.TripList.as_view()),
    path('trips-create/', trip.TripCreate.as_view()),
    path("get-places/", api_test.api_test),
        
    
    path("login/", views.login_handler, name="login"),
    path("logout/", views.logout_handler, name="logout"),
    path("budget/", views.budget_handler, name="budeget"),
    path("checklist/", views.checklist_handler, name="checklist"),
    path("trip/", views.trip_handler, name="trip"),
    path("duration/", views.duration_handler, name="duration"),
    path("home/", views.home_handler, name="home"),
    path("itinerary/", views.itinerary_handler, name="itinerary"),
    path("landing/", views.landing_handler, name="landing"),
    path("map/", views.map_handler, name="map"),
    path("messaging/", views.messaging_handler, name="messaging"),
    path("settings/", views.settings_handler, name="settings"),
    path("weather/", views.weather_handler, name="weather"),
]
