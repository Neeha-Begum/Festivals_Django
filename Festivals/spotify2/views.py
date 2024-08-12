from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    return HttpResponse("modhera dance festival")
def wish2(request):
    return HttpResponse("Kite festival")
def wish3(request):
    return HttpResponse("Rann Utsav")
def wish4(request):
    return HttpResponse("Bhadra Purnima")