from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request):
    return HttpResponse("Happy Baisakhi Festival!")
def wish2(request):
    return HttpResponse("Surajkund craft mela")
def wish3(request):
    return HttpResponse("Lohri")
def wish4(request):
    return HttpResponse("Haryana Day")