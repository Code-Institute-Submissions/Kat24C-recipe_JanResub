from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_break, name='recipe-home-pg'),
    path('review/', views.recipe_review, name='recipe-review-pg'),
]
