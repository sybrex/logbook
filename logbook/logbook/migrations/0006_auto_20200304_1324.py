# Generated by Django 3.0.3 on 2020-03-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0005_auto_20200304_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.IntegerField(unique=True),
        ),
    ]
