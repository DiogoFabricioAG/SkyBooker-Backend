# Generated by Django 5.0.3 on 2024-03-16 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='image',
            field=models.ImageField(default=1, upload_to='hotel/'),
            preserve_default=False,
        ),
    ]