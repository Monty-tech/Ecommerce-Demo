# Generated by Django 3.2.4 on 2021-08-29 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECOM', '0002_remove_products_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
