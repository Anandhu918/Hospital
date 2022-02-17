# Generated by Django 4.0.1 on 2022-02-08 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0020_med_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='warning',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
