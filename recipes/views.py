from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from . import models
from .forms import ReviewDetail
# Create your views here.


def recipe_break(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_home.html', context)


class recipe_full(ListView):
    model = models.Recipe
    template_name = 'recipe_home.html'
    context_object_name = 'recipes'


def fullview(request, pk):
    model = models.Recipe
    recipe = get_object_or_404(model, pk=pk)
    return render(request, 'full_recipe.html', {'recipe': recipe})

