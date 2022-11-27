from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecipePost.as_view(), name="home"),
]
