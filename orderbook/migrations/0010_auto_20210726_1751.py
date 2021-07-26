# Generated by Django 3.1.6 on 2021-07-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderbook', '0009_tradingpair_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('market', 'Market'), ('limit', 'Limit')], default='limit', max_length=200),
        ),
    ]