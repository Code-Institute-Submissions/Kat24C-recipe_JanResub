from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Recipe_pg(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    recipe_description = models.CharField(max_length=200)
    preparation_cooking_time = models.CharField(max_length=100)
    ingredient = models.TextField(max_length=60)
    directions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    author = models.ForeignKey(Recipe_pg, on_delete=models.CASCADE)
    email = models.EmailField()
    comment = models.TextField(max_length=250)
    date_published = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment {self.comment} by {self.author}"
