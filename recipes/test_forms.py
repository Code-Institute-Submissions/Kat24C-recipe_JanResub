from django.test import TestCase
from .forms import RecipeDetail


class TestForms(TestCase):

    def test_recipe_detail(self):
        form = RecipeDetail({'name': '', 'ingredients': '', 'directions': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_recipe_metaclass(self):
        form = RecipeDetail()
        self.assertEqual(form.Meta.fields, (
            'name',
            'recipe_description',
            'preparation',
            'ingredient',
            'directions'))
