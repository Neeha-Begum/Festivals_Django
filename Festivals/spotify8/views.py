from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request):
    return HttpResponse("Durga Puja")
def wish2(request):
    return HttpResponse("Nandikar National Theatre Festival")
def wish3(request):
    return HttpResponse("Kali Puja")
def wish4(request):
    return HttpResponse("Ganga Sagar Mela")