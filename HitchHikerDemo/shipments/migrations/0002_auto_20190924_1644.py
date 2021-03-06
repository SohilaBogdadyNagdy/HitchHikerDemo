# Generated by Django 2.0.8 on 2019-09-24 16:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='dimension',
        ),
        migrations.AddField(
            model_name='shipment',
            name='dimensions',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(verbose_name='Dimensions'), size=None), default=[0, 0], size=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shipment',
            name='is_delivered',
            field=models.CharField(max_length=255, verbose_name='is_delivered'),
        ),
    ]
