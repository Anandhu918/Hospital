# Generated by Django 4.0.1 on 2022-02-07 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0019_remove_products_nos_products_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='med_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.IntegerField()),
                ('p_name', models.CharField(max_length=100)),
                ('p_description', models.TextField()),
                ('p_price', models.IntegerField()),
            ],
        ),
    ]