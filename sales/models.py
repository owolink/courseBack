from django.db import models
from category.models import Category

class Sales(models.Model):
    title = models.CharField(verbose_name='Name', max_length=255)
    category = models.ManyToManyField(to=Category, related_name='sales', verbose_name='category')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
