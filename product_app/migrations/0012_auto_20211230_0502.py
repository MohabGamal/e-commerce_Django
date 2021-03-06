# Generated by Django 3.2.9 on 2021-12-30 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0011_productgallary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productgallary',
            old_name='destination',
            new_name='product',
        ),
        migrations.AddField(
            model_name='productgallary',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
