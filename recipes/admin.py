from django.contrib import admin
from .models import Recipe, Reviews


@admin.register(Recipe)
class RecipeThings(admin.ModelAdmin):
    list_display = ('name', 'recipe_description', 'preparation')


@admin.register(Reviews)
class Review_outline(admin.ModelAdmin):
    list_display = ('author', 'comment')
    