# Generated by Django 3.1.3 on 2020-11-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_description',
            field=models.CharField(max_length=500),
        ),
    ]
