# Generated by Django 3.1.3 on 2020-11-19 19:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20201114_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
