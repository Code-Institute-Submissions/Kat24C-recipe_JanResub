from django.test import TestCase
from django.urls import reverse
from .models import Recipe
from django.contrib.auth.models import User
from . import views


class TestViews(TestCase):

    def test_recipe_break_works(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_home.html')

    def test_get_add_recipe_page(self):
        response = self.client.get('/add/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_add_recipe_items(self):
        response = self.client.post('/add/', {'name': 'Recipe Test'})
        self.assertRedirects(response, '/')

    def test_get_update_page(self):
        test_user = User.objects.create_user(username='testname')
        author = Recipe.objects.create(author=test_user)
        recipe = Recipe.objects.create(name='Test Recipe')
        response = self.client.get(f'/edit/{recipe.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_recipe.html')

    def test_delete_recipe_page(self):
        test_recipe = Recipe.objects.create(name='Test Recipe')
        response = self.client.get(f'/delete/{test_recipe.id}')
        self.assertEqual(response.status_code, 200)

    def test_search_recipe_page(self):
        response = self.client.get('/search_recipe/')
        self.assertEqual(response.status_code, 200)
