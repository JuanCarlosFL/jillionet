# Generated by Django 3.1.6 on 2021-07-29 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_userbalance_public_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_level_field',
            old_name='Margin_leverage',
            new_name='Jillion_hold_trigger',
        ),
        migrations.RenameField(
            model_name='user_level_field',
            old_name='inicial_balance_JILL',
            new_name='free_balance_JILL',
        ),
        migrations.RenameField(
            model_name='user_level_field',
            old_name='margin_call',
            new_name='maker_taker',
        ),
        migrations.RemoveField(
            model_name='user_level_field',
            name='max_withdraw_JILL',
        ),
        migrations.RemoveField(
            model_name='user_level_field',
            name='spred',
        ),
    ]
