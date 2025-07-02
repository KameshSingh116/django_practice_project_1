from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

def home(request):
    return  HttpResponse("This is the home page of the 1st django practice project.")

def recipies(request):
    if request.method=="POST":

      data=request.POST
      recipe_image=request.FILES.get('recipe_image')
      recipe_name=data.get('recipe_name')
      recipe_description=data.get('recipe_description')
     
      
      recipe.objects.create (
         recipe_name=recipe_name,
         recipe_description=recipe_description,
         recipe_image=recipe_image
      )

      return redirect('/recipies')
    queryset=recipe.objects.all()
    context={'recipies':queryset}


    return render(request, "recipies.html",context)

def delete_recipe(request, id):
      queryset=recipe.objects.get(id = id)
      queryset.delete()
      return redirect('/recipies/')