from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request) :
    return render(request, 'home/index.html')

def aboutus(request) :
    return render(request, 'footer/about.html')


def contactus(request) :
    return render(request, 'footer/contactus.html')