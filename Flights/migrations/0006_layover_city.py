# Generated by Django 5.0.3 on 2024-03-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flights', '0005_flight_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='layover',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
