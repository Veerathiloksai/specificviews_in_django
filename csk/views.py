from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def captain(request):
    return HttpResponse("<h1><marquee>Rutu-Raja is captain of CSK💛💛")

def vicecaptain(request):
    return HttpResponse("<h1><marquee>Jaddu is vice-captain of CSK")

