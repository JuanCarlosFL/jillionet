# Generated by Django 3.1.6 on 2021-09-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210825_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbalance',
            name='action',
            field=models.CharField(choices=[('deposit', 'Deposit'), ('withdraw', 'Withdraw'), ('transfer', 'Transfer')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userbalance',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
