# Generated by Django 4.0.4 on 2022-06-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='pics/'),
        ),
    ]
