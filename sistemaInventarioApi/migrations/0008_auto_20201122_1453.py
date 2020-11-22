# Generated by Django 3.1.2 on 2020-11-22 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaInventarioApi', '0007_auto_20201122_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='idProducto',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='idCliente',
            new_name='Cliente',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='idVendedor',
            new_name='Vendedor',
        ),
        migrations.RenameField(
            model_name='facturadetalle',
            old_name='idDescuento',
            new_name='Descuento',
        ),
        migrations.RenameField(
            model_name='facturadetalle',
            old_name='idFactura',
            new_name='factura',
        ),
        migrations.RenameField(
            model_name='facturadetalle',
            old_name='idProducto',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='idProducto',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='idProveedor',
            new_name='proveedor',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='idProducto',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='salida',
            old_name='idFactura',
            new_name='factura',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='idProveedor',
        ),
        migrations.AddField(
            model_name='pedido',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Proveedor', to='sistemaInventarioApi.usuario'),
            preserve_default=False,
        ),
    ]