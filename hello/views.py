import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'hello/home.html')

def register(request):
    return render(request, 'hello/register.html')

def booking(requst):
    return render(requst, 'hello/booking.html')