# Generated by Django 4.2.5 on 2024-03-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='allergy',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
