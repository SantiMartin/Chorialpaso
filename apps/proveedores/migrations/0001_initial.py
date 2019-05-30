# Generated by Django 2.2 on 2019-05-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellidos', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=110)),
                ('mail', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.CharField(max_length=20, unique=True)),
                ('telefono2', models.CharField(blank=True, max_length=20, unique=True)),
                ('producto', models.ManyToManyField(to='stock.Producto')),
            ],
        ),
    ]
