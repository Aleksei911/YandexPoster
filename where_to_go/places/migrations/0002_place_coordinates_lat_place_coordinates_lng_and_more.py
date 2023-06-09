# Generated by Django 4.1.7 on 2023-03-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='coordinates_lat',
            field=models.CharField(default=1, max_length=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='coordinates_lng',
            field=models.CharField(default=1, max_length=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='description_long',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='description_short',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
