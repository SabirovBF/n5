# Generated by Django 5.0.6 on 2024-05-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
            ],
            options={
                'verbose_name': 'Рабочий',
                'verbose_name_plural': 'Рабочии',
            },
        ),
    ]