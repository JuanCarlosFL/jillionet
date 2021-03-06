# Generated by Django 3.1.6 on 2021-09-18 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210911_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_key', models.CharField(max_length=200, unique=True)),
                ('borrow_interest', models.CharField(max_length=200, unique=True)),
                ('maker_taker', models.CharField(max_length=200, unique=True)),
                ('inicial_balance_USDT', models.CharField(max_length=200, unique=True)),
                ('free_balance_JILL', models.DecimalField(decimal_places=18, default=0, max_digits=36)),
                ('max_withdraw_USDT', models.CharField(max_length=200, unique=True)),
                ('Jillion_hold_trigger', models.DecimalField(decimal_places=18, default=0, max_digits=36)),
                ('Futures_leverage', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User_level_field',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_level',
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.userlevel'),
        ),
    ]
