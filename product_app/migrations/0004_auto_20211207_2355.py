# Generated by Django 3.2.9 on 2021-12-07 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_product_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ratings',
            field=models.IntegerField(null=True),
        ),
    ]
