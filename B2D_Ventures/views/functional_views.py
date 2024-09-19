from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request) -> HttpResponse:
    return render(request, "index.html")


def details(request):
    return render(request, 'details.html')


def profile(request):
    return render(request, "profile.html")
