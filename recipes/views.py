from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from . import models
from django.core.paginator import Paginator
from .forms import RecipeDetail
# Create your views here.


def recipe_break(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    recipe_list = models.Recipe.objects.all()
    paginator = Paginator(recipe_list, 3)
    return render(request, 'recipe_home.html', context)


class recipe_full(generic.ListView):
    model = models.Recipe
    template_name = 'recipe_home.html'
    context_object_name = 'recipes'
 

def fullview(request, pk):
    model = models.Recipe
    recipe = get_object_or_404(model, pk=pk)
    return render(request, 'full_recipe.html', {'recipe': recipe})


def add_recipe(request, *args, **kwargs):
    adding_recipe = RecipeDetail()
    if request.method == "POST":
        adding_recipe = RecipeDetail(request.POST)
        if adding_recipe.is_valid():
            r = adding_recipe.save(commit=False)
            r.author = request.user
            r.Recipe = models.Recipe
            r.save()

        return redirect(reverse('recipe-home-pg'))

    return render(request, 'add_recipe.html', {"adding_recipe": adding_recipe})


def update_recipe(request, recipe_id):
    rec = models.Recipe.objects.get(pk=recipe_id)
    form = RecipeDetail(request.POST or None, instance=rec)
    if form.is_valid():
        form.save()
        return redirect(reverse('recipe-home-pg'))

    return render(request, 'edit_recipe.html', {'rec': rec, 'form': form})


def delete_recipe(request, recipe_id):
    del_rec = models.Recipe.objects.get(pk=recipe_id)
    if request.method == "POST":
        del_rec.delete()
        return redirect(reverse('recipe-home-pg'))

    return render(request, 'delete_recipe.html', {'del_rec': del_rec})


def recipe_search(request):
    search = request.GET.get('search', '')
    if search:
        srecipes = models.Recipe.objects.filter(name__icontains=search)
        return render(request, 'search_recipe.html', {
            'search': search, 'srecipes': srecipes})
    else:
        return render(request, 'search_recipe.html', {})
