from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request):
    return HttpResponse("Konark Festival")
def wish2(request):
    return HttpResponse("International Sand Art Festival")
def wish3(request):
    return HttpResponse("Shiva Ratri")
def wish4(request):
    return HttpResponse("Dola Purnima (Holi)")