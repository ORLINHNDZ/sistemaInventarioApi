# Generated by Django 3.1.2 on 2021-01-09 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaInventarioApi', '0022_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]