from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.


def recipe_break(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_home.html', context)


def recipe_review(request):
    reviews = models.Reviews.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'recipe_reviews.html', context)
