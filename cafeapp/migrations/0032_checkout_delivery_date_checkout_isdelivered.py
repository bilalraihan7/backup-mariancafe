# Generated by Django 4.1.13 on 2024-03-03 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0031_foodmenu_removalstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='isDelivered',
            field=models.CharField(default='Delivered', max_length=20),
        ),
    ]
