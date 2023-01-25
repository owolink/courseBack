# Generated by Django 4.1.5 on 2023-01-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name')),
                ('category', models.CharField(max_length=255, verbose_name='Category')),
                ('photo', models.ImageField(upload_to='recipies', verbose_name='Photo')),
                ('product', models.CharField(max_length=255, verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipies',
            },
        ),
    ]
