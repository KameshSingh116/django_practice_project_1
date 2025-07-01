from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return  HttpResponse("This is the home page of the 1st django practice project.")

def recipies(request):
    
    return render(request, "recipies.html")
