# Generated by Django 4.0.1 on 2022-01-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='films',
            field=models.ManyToManyField(to='film.Film'),
        ),
    ]
