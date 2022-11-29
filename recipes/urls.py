from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_break, name='recipe-home-pg'),
]
