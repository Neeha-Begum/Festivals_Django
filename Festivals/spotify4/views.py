from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request):
    return HttpResponse("jiviputrika Festival")
def wish2(request):
    return HttpResponse("Bihula")
def wish3(request):
    return HttpResponse("Sonepur Cattle Fair")
def wish4(request):
    return HttpResponse("Buddha Jayanti")