from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def user(request):
    return render(request, "user.html")

def search(request):
    return render(request, "search.html")