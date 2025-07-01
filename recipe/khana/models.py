from django.db import models

# Create your models here.
class recipe(models.Model):
    recipe_name=models.CharField(max_length=100)
    recipe_description=models.TextField(max_length=1000)
    recipe_image=models.ImageField(upload_to="recipe_folder")