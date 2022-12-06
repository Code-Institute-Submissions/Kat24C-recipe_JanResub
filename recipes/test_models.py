from django.test import TestCase
from django.urls import path, reverse
from .models import Recipe
from . import views


class TestRecipe(TestCase):
    def setUp(self):
        Recipe.objects.create(name="Tester")

    def test_recipe_string_method_returns_name(self):
        recipe = Recipe.objects.create(name='Test Recipe')
        self.assertEqual(str(recipe), 'Test Recipe')

    def test_recipe_view(self):
        recipe = Recipe.objects.get(name="Tester")
        url = reverse("recipes-full", args=[recipe.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'full_recipe.html')
