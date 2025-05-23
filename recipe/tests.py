from django.test import TestCase
from django.db import IntegrityError
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Десерти')
        self.assertEqual(category.name, 'Десерти')

    def test_category_unique_name(self):
        Category.objects.create(name='Сніданки')
        with self.assertRaises(IntegrityError):
            Category.objects.create(name='Сніданки')

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Головні страви')

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title='Салат Цезар',
            description='Класичний рецепт салату Цезар',
            instructions='Наріжте салат',
            ingredients='Салат, куряче філе',
            category=self.category
        )
        self.assertEqual(recipe.description, 'Класичний рецепт салату Цезар')

    def test_recipe_null_description(self):
        recipe = Recipe.objects.create(
            title='Омлет',
            instructions='Взбейте яйца',
            ingredients='Яйца, молоко',
            category=self.category,
        )
        self.assertIsNone(recipe.description)

    def test_recipe_auto_datetime(self):
        recipe = Recipe.objects.create(
            title='Пиріг',
            instructions='В духовку',
            ingredients='Борошно, цукор',
            category=self.category
        )
        self.assertIsNotNone(recipe.created_at)

    def test_recipe_update_auto_datetime(self):
        recipe = Recipe.objects.create(
            title='Каша',
            instructions='Сварить',
            ingredients='Крупа, вода',
            category=self.category
        )
        initial_updated_at = recipe.updated_at
        self.assertIsNotNone(initial_updated_at)
        recipe.title = 'Каша с молоком'
        recipe.save()
        self.assertGreater(recipe.updated_at, initial_updated_at)