# Generated by Django 3.1.2 on 2020-11-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaInventarioApi', '0008_auto_20201122_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='existencia',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
