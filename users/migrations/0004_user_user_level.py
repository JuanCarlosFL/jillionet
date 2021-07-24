# Generated by Django 3.1.6 on 2021-07-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210722_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.CharField(choices=[('diamond', 'Diamond'), ('gold', 'Gold'), ('silver', 'Silver'), ('copper', 'Copper'), ('platinum', 'Platinum'), ('bronze', 'Bronze')], default='bronze', max_length=50),
        ),
    ]
