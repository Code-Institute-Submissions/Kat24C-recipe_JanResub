from django.shortcuts import render
from django.views import generic
from .models import Recipe_pg
# Create your views here.


def recipe_break(request):
    recipe = Recipe_pg.objects.all()
    context = {
        'recipe': recipe
    }
    return render(request, 'recipes/base.html', context)


class RecipePost(generic.ListView):
    model = Recipe_pg
    template_engine = 'index.html'
    paginate_by = 5
