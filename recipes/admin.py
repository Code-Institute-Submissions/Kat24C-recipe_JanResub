from django.contrib import admin
from .models import Recipe_pg, Reviews


@admin.register(Recipe_pg)
class RecipeThings(admin.ModelAdmin):
    list_display = ('name', 'recipe_description', 'preparation_cooking_time')
    summernote_fields = ('content')


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment')
