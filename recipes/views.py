from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from . import models
from django.core.paginator import Paginator
from .forms import RecipeDetail
# Create your views here.


# Links to recipe home: a break down of the recipes.
def recipe_break(request):
    recipes = models.Recipe.objects.all().order_by('id')
    num = Paginator(recipes, 4)
    page = request.GET.get('page')
    recpage = num.get_page(page)
    context = {
        'recipes': recipes,
        'recpage': recpage
    }
    return render(request, 'recipe_home.html', context)


class recipe_full(generic.ListView):
    model = models.Recipe
    template_name = 'recipe_home.html'
    context_object_name = 'recipes'


# A link to view the full recipe.
def fullview(request, pk):
    model = models.Recipe
    recipe = get_object_or_404(model, pk=pk)
    return render(request, 'full_recipe.html', {'recipe': recipe})


# A link to add the recipes, only when signed in.
def add_recipe(request, *args, **kwargs):
    if request.user.is_authenticated:
        adding_recipe = RecipeDetail()
        if request.method == "POST":
            adding_recipe = RecipeDetail(request.POST)
            if adding_recipe.is_valid():
                r = adding_recipe.save(commit=False)
                r.author = request.user
                r.Recipe = models.Recipe
                r.save()
            
            return redirect(reverse('recipe-home-pg'))
    else:

        return redirect(reverse('recipe-home-pg'))

    return render(request, 'add_recipe.html', {"adding_recipe": adding_recipe})


# Author can update their recipe and returns to home page.
def update_recipe(request, recipe_id):
    rec = models.Recipe.objects.get(pk=recipe_id)
    if request.user.id == rec.author.id:
        form = RecipeDetail(request.POST or None, instance=rec)
        if form.is_valid():
            form.save()
            return redirect(reverse('recipe-home-pg'))
    else:
        return redirect(reverse('recipe-home-pg'))

    return render(request, 'edit_recipe.html', {'rec': rec, 'form': form})


# Author is able to delete their recipe.
def delete_recipe(request, recipe_id):
    del_rec = models.Recipe.objects.get(pk=recipe_id)
    if request.user.id == del_rec.author.id:
        if request.method == "POST":
            del_rec.delete()
            return redirect(reverse('recipe-home-pg'))
    else:
        return redirect(reverse('recipe-home-pg'))

    return render(request, 'delete_recipe.html', {'del_rec': del_rec})


# A simple search bar, that isnot case sensitive.
def recipe_search(request):
    search = request.GET.get('search', '')
    if search:
        srecipes = models.Recipe.objects.filter(name__icontains=search)
        return render(request, 'search_recipe.html', {
            'search': search, 'srecipes': srecipes})
    else:
        return render(request, 'search_recipe.html', {})
