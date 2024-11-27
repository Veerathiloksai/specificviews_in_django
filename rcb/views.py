from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def captain(request):
    return HttpResponse("<h1><marquee>Kohli is captain of RCB")

def vicecaptain(request):
    return HttpResponse("<h1><marquee>DK is vice-captain of RCB")
