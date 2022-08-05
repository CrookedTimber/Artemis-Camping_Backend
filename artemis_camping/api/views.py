from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Home</h1>")

def simple_view(request):
    return HttpResponse("<h1>Test View</h1>")

def simple_view2(request):
    return HttpResponse("<h1>Second Test View</h1>")
