# Generated by Django 3.2.9 on 2021-12-30 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0010_alter_product_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='Product_gallary')),
                ('destination', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product_app.product')),
            ],
        ),
    ]
