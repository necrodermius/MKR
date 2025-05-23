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
