# Generated by Django 5.0.6 on 2024-05-10 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_times_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matematic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
            ],
            options={
                'verbose_name': 'Переворот',
                'verbose_name_plural': 'Переворот',
            },
        ),
        migrations.AlterModelOptions(
            name='times',
            options={'verbose_name_plural': datetime.datetime(2024, 5, 10, 21, 20, 12, 784113)},
        ),
    ]
