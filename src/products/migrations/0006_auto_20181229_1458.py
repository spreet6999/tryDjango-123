# Generated by Django 2.0.7 on 2018-12-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
