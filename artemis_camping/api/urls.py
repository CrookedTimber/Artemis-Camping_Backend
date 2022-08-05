from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view/", views.second_view, name="view"),
    path("vista/", views.vista, name="vista"),
]
