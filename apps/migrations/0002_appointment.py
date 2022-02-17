# Generated by Django 4.0 on 2022-01-18 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('slot_1', models.IntegerField(default=0)),
                ('slot_2', models.IntegerField(default=0)),
                ('slot_3', models.IntegerField(default=0)),
                ('slot_4', models.IntegerField(default=0)),
                ('slot_5', models.IntegerField(default=0)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.doctor')),
            ],
        ),
    ]