# Generated by Django 4.0.1 on 2022-01-27 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
