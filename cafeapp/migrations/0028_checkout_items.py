# Generated by Django 4.2.7 on 2024-02-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0027_remove_checkout_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='items',
            field=models.ManyToManyField(to='cafeapp.foodmenu'),
        ),
    ]
