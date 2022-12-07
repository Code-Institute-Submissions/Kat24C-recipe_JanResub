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
