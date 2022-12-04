from django.urls import path
from . import views

'full_recipe.html'
'edit_recipe.html'


urlpatterns = [
    path('', views.recipe_break, name='recipe-home-pg'),
    path('recipe/<int:pk>', views.fullview, name='recipes-full'),
    path('add/', views.AddRecipe, name='recipes-add'),
    path('edit/<recipe_id>', views.update_recipe, name='recipes-edit'),
    
]
