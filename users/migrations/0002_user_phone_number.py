# Generated by Django 3.1.6 on 2021-07-22 12:52

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+2348123020789', max_length=128, region=None),
            preserve_default=False,
        ),
    ]
