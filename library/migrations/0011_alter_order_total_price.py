# Generated by Django 5.1.3 on 2024-11-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(),
        ),
    ]
