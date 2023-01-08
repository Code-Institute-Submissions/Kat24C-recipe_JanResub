from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeThings(admin.ModelAdmin):
    """
    Admin access to models.py basics: name, description
    and preparation. Created a superuser.
    """
    list_display = ('name', 'recipe_description', 'preparation')


