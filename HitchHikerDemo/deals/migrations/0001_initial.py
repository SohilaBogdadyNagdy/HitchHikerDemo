# Generated by Django 2.0.8 on 2018-09-24 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trips', '0001_initial'),
        ('shipments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField(verbose_name='Transfer Cost')),
                ('is_traveler_confirmed', models.BooleanField(default=False)),
                ('is_shipper_confirmed', models.BooleanField(default=False)),
                ('shipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipments.Shipment')),
                ('trip_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip')),
            ],
        ),
    ]
