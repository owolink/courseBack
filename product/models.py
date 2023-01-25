from django.db import models
from authentication.models import User
from customer.models import Customer

class Product(models.Model):
    title = models.CharField(verbose_name='Name', max_length=255)
    customer = models.ManyToManyField(to=Customer, related_name='product', verbose_name='customer')
    photo = models.ImageField(verbose_name='Photo', upload_to='products')
    description = models.TextField(verbose_name='Description')
    ingridients = models.TextField(verbose_name='Ingridients')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class FavouriteProduct(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)