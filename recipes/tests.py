from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipe_home_URL_is_correct(self):
        url = reverse("recipes:home")
        self.assertEqual(url, '/')

    def test_recipe_category_home_URL_is_correct(self):
        url = reverse("recipes:category", args=(1,))
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_page_URL_is_correct(self):
        url = reverse("recipes:recipe", args=(3,))
        self.assertEqual(url, '/recipes/3/')
