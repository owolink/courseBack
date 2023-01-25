from django.db import models
from product.models import Product

class Category(models.Model):
    title = models.CharField(verbose_name='Name', max_length=255)
    country = models.CharField(verbose_name='Country', max_length=255)
    photo = models.ImageField(verbose_name='Photo', upload_to='category')
    description = models.TextField(verbose_name='Description')
    product = models.ManyToManyField(to=Product, verbose_name='product', related_name='product')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
