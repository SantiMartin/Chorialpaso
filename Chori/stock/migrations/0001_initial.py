# Generated by Django 2.1.7 on 2019-03-26 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('descripcion_categoria', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('telefono', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formato',
            fields=[
                ('id_formato', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('descripcion_formato', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad_producto', models.IntegerField()),
                ('precio_costo', models.FloatField()),
                ('precio_venta', models.FloatField()),
                ('tipo_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Categoria')),
                ('tipo_formato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Formato')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoXProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('costo', models.FloatField()),
                ('fecha_entrada', models.DateField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=80)),
                ('apellidos', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=110)),
                ('mail', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='productoxproveedor',
            name='id_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Proveedor'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='id_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Proveedor'),
        ),
    ]
