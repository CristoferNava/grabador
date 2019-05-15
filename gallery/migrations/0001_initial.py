# Generated by Django 2.0.2 on 2019-05-15 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('image', models.ImageField(upload_to='store', verbose_name='Imagen')),
                ('price', models.CharField(max_length=10, verbose_name='Precio')),
                ('technique', models.CharField(max_length=100, verbose_name='Técnica')),
                ('size', models.CharField(max_length=100, verbose_name='Dimensiones')),
                ('url', models.URLField(verbose_name='Link de venta')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Obra',
                'verbose_name_plural': 'Obras',
            },
        ),
    ]
