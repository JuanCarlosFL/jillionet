# Generated by Django 3.1.6 on 2021-07-29 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderbook', '0014_currency_last_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='contract_creator_hash',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
