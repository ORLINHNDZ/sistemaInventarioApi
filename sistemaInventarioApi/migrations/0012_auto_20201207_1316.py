# Generated by Django 3.1.2 on 2020-12-07 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaInventarioApi', '0011_auto_20201206_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipoProducto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistemaInventarioApi.tipoproducto'),
        ),
    ]