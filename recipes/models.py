from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Recipe(models.Model):
    """
    A recipe model asking for the basic needs of a recipe.
    Include name, preparation, ingredients and directions.
    Giving a big space for the ingredients and directions.
    """
    name = models.CharField(max_length=100, unique=True, blank=False)
    recipe_description = models.CharField(max_length=200)
    preparation = models.CharField(max_length=100)
    ingredient = models.TextField(max_length=600)
    directions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def getFull(self):
        return reverse("recipes-full", kwargs={"pk": self.pk})
