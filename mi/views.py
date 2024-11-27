from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def captain(request):
    return HttpResponse("<h1><marquee>Hardik is captain of MI")

def vicecaptain(request):
    return HttpResponse("<h1><marquee>Boom is vice-captain of MI")
