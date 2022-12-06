from django.test import TestCase
from .models import Recipe


class TestViews(TestCase):

    def test_recipe_break_works(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_home.html')

    def test_get_add_recipe_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_get_edit_recipe_page(self):
        recipe = Recipe.objects.create(name='Test Recipe')
        response = self.client.get(f'edit/{recipe_id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_recipe.html')
