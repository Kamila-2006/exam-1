# Generated by Django 5.1.3 on 2024-12-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_rename_type_meal_meal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]