# Generated by Django 3.2.6 on 2021-08-31 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
