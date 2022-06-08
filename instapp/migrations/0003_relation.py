# Generated by Django 4.0.4 on 2022-06-08 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0002_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='instapp.profile')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='instapp.profile')),
            ],
            options={
                'unique_together': {('followers', 'following')},
            },
        ),
    ]