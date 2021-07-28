# Generated by Django 3.1.6 on 2021-07-26 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderbook', '0011_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='volume',
            field=models.DecimalField(decimal_places=18, default=10000, max_digits=36),
        ),
    ]
