# Generated by Django 3.1.6 on 2021-07-24 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderbook', '0002_auto_20210724_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='contract_type',
            field=models.CharField(choices=[('spot', 'Spot'), ('futures', 'Futures')], default='spot', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('market', 'Market'), ('limit', 'Limit')], default='market', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('fill', 'Fill')], default='new', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orderbook.currency'),
        ),
    ]
