from django.shortcuts import render

# Create your views here.


def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')


def create(request, *args, **kwargs):
    return render(request, 'frontend/CreateEventPage.html')


def welcome(request, *args, **kwargs):
    return render(request, 'frontend/witaj.html')


def login(request, *args, **kwargs):
    return render(request, 'frontend/zaloguj.html')
