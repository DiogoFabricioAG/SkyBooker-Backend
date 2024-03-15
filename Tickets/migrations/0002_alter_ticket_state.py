# Generated by Django 5.0.3 on 2024-03-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='state',
            field=models.CharField(choices=[('Active', 'Active'), ('Used', 'Used'), ('Inactive', 'Inactive')], default='Active', max_length=15),
        ),
    ]
