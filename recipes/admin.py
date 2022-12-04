from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeThings(admin.ModelAdmin):
    list_display = ('name', 'recipe_description', 'preparation')

