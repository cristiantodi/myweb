# Generated by Django 4.1.dev20211123065844 on 2022-07-15 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedido',
            old_name='pedido_id',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='lineapedido',
            old_name='producto_id',
            new_name='producto',
        ),
        migrations.AlterModelTable(
            name='lineapedido',
            table='Linea Pedido',
        ),
    ]
