from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Othest home")

def dynamic_path(request):
    return HttpResponse("View")

def vista(request):
    return HttpResponse("Vista")
