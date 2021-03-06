# Generated by Django 3.1.6 on 2021-07-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='iabotcontract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractnumber', models.CharField(max_length=200, unique=True)),
                ('pair', models.CharField(max_length=200, unique=True)),
                ('timeframe', models.CharField(max_length=200, unique=True)),
                ('win_close_point', models.CharField(max_length=200, unique=True)),
                ('lose_close_point', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='iabotOrderbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair', models.CharField(max_length=200, unique=True)),
                ('volume', models.CharField(max_length=200, unique=True)),
                ('buy_sell', models.CharField(max_length=200, unique=True)),
                ('loop_time_frame', models.CharField(max_length=200, unique=True)),
                ('random_spred', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
