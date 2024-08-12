from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request):
    return HttpResponse("ramazan")
def wish2(request):
    return HttpResponse("dussera")
def wish3(request):
    return HttpResponse("Vinayaka Chaturthi")
def wish4(request):
    return HttpResponse("Ugadi")