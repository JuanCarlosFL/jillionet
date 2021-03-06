# Generated by Django 3.1.6 on 2021-08-25 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210824_0707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userbalance',
            options={'ordering': ['user', 'currency__code']},
        ),
        migrations.AddField(
            model_name='userbalance',
            name='staked',
            field=models.DecimalField(decimal_places=18, default=0, max_digits=36),
        ),
    ]
