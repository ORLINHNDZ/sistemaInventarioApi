# Generated by Django 3.1.2 on 2021-01-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaInventarioApi', '0019_auto_20201223_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
