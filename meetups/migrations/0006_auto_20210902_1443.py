# Generated by Django 3.2.6 on 2021-09-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_auto_20210902_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-03-04'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='test@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, to='meetups.Participant'),
        ),
    ]
