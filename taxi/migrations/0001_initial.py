# Generated by Django 5.1.3 on 2024-12-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxi_name', models.CharField(max_length=50)),
                ('license_plate', models.CharField(max_length=10)),
                ('driver_name', models.CharField(max_length=50)),
                ('passenger_capacity', models.PositiveIntegerField()),
                ('car_model', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Select Status', 'Select Status'), ('Available', 'Available'), ('Busy', 'Busy'), ('Under Maintenance', 'Under Maintenance')], max_length=20)),
            ],
        ),
    ]
