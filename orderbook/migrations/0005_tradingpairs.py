# Generated by Django 3.1.6 on 2021-07-25 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderbook', '0004_auto_20210724_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='tradingPairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]