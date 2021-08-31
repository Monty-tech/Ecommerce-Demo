# Generated by Django 3.2.4 on 2021-08-31 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECOM', '0007_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]