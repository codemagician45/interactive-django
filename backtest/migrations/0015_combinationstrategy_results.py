# Generated by Django 2.2.1 on 2019-11-18 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backtest', '0014_auto_20191116_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='combinationstrategy',
            name='results',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='backtest.Result'),
        ),
    ]