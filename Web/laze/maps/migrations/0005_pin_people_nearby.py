# Generated by Django 2.1.2 on 2018-11-22 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_auto_20181122_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='people_nearby',
            field=models.IntegerField(default=0),
        ),
    ]