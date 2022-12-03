from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    recipe_description = models.CharField(max_length=200)
    preparation = models.CharField(max_length=100)
    ingredient = models.TextField(max_length=600)
    directions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def getFull(self):
        return reverse("recipe-full", kwargs={"pk": self.pk})


class Reviews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    comment = models.TextField(max_length=250)
    date_published = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment {self.comment} by {self.author}"
