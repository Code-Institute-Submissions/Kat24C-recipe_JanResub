from django.urls import path
from . import views

'full_recipe.html'
'edit_recipe.html'


urlpatterns = [
    path('recipes_break', views.recipe_break, name='recipes_break'),
    path('', views.recipe_break, name='recipe-home-pg'),
    path('recipe/<int:pk>', views.fullview, name='recipes-full'),
    path('add/', views.add_recipe, name='recipes-add'),
    path('edit/<recipe_id>', views.update_recipe, name='recipes-edit'),
    path('delete/<recipe_id>', views.delete_recipe, name='recipe-delete'),
    path('search_recipe/', views.recipe_search, name='search-recipe'),
]
