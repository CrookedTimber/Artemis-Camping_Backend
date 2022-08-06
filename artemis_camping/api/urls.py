from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view/", views.simple_view, name="view"),
    path("view2/", views.simple_view2, name="vista"),
]
