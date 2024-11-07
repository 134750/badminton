# Generated by Django 5.2.dev20241101104349 on 2024-11-07 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badminton', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='hide_score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
