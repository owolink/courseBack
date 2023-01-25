from django.db import models
from product.models import Product

class Recipies(models.Model):
    title = models.CharField(verbose_name='Name', max_length=255)
    photo = models.ImageField(verbose_name='Photo', upload_to='recipies')
    product = models.ManyToManyField(to=Product, related_name='recipes', verbose_name='product')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipies'