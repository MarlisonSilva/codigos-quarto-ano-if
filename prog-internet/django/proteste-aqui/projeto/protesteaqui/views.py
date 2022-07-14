import site
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    return HttpResponse('Olá!')

def home(request):
    site = "<html><body> <h1>HOME</h1> </body></html>" , datetime.now().strftime('%H:%M:%S')
    return HttpResponse(site)