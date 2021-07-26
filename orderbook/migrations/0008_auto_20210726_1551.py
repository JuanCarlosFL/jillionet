# Generated by Django 3.1.6 on 2021-07-26 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderbook', '0007_currency_chain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='currency',
        ),
        migrations.AddField(
            model_name='order',
            name='trading_pair',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orderbook.tradingpair'),
        ),
    ]