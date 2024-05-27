# Generated by Django 4.2.5 on 2024-03-23 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_time_numberofpeoplemax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='photo',
        ),
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='menu',
            name='upload_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 23, 8, 22, 13, 354306, tzinfo=datetime.timezone.utc)),
        ),
    ]