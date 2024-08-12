from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request):
    return HttpResponse("Pongal")
def wish2(request):
    return HttpResponse("Natyanjali Festival")
def wish3(request):
    return HttpResponse("Natyanjali Dance Festival")
def wish4(request):
    return HttpResponse("Thiruvaiyaru Festival")