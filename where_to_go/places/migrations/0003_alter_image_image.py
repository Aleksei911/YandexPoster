# Generated by Django 4.1.7 on 2023-03-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='places/static/img/'),
        ),
    ]
