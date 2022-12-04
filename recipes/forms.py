from .models import Recipe
from django import forms


class RecipeDetail(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'recipe_description', 'preparation', 'ingredient', 'directions',)
