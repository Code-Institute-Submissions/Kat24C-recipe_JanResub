from .models import Recipe
from django import forms


# A basic form for a recipe.
class RecipeDetail(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'name',
            'recipe_description',
            'preparation',
            'ingredient',
            'directions',
        )
