from django.urls import path
from . import views

'full_recipe.html'

urlpatterns = [
    path('', views.recipe_break, name='recipe-home-pg'),
    path('recipe/<int:pk>', views.fullview, name='recipes-full'),
]
