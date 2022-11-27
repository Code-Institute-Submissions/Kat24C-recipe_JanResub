from django.contrib import admin
from .models import Recipe_pg, Reviews
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe_pg)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('name', 'recipe_description', 'preparation_cooking_time')
    summernote_fields = ('content')


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment')
