from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Recipe(models.Model):
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
        return reverse("recipe-full", kwargs={"pk": self.pk})
