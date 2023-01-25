# Generated by Django 4.1.5 on 2023-01-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('photo', models.ImageField(upload_to='category', verbose_name='Photo')),
                ('description', models.TextField(verbose_name='Description')),
                ('product', models.ManyToManyField(related_name='product', to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
