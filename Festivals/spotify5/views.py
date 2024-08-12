from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    return HttpResponse("Tejaji Fair")
def wish2(request):
    return HttpResponse("Khajuraho Festival")
def wish3(request):
    return HttpResponse("Lokranjan or Khajuraho Festival")
def wish4(request):
    return HttpResponse("Bhagoria Haat Festival")