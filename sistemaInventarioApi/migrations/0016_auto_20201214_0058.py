# Generated by Django 3.1.2 on 2020-12-14 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaInventarioApi', '0015_auto_20201210_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='isActive',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='isAdmin',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='roles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistemaInventarioApi.roles'),
        ),
    ]
