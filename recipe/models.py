from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name='Назва категорії')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']

    def __iter__(self):
        return self

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField()
    ingredients = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='recipes',
        verbose_name='Категорія'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепти'

    def __str__(self):
        return self.title