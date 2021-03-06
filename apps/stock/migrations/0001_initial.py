# Generated by Django 2.1.7 on 2019-06-04 14:23

import datetime
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_categoria', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Modificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=80)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad_producto', models.IntegerField(default=0)),
                ('tipo_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='modificacion',
            name='codigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Producto'),
        ),
    ]
