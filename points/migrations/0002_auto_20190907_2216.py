# Generated by Django 2.2.3 on 2019-09-08 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oaxaca',
            options={'verbose_name': 'Imagen Oaxaca', 'verbose_name_plural': 'Imágenes Oaxaca'},
        ),
        migrations.AlterModelOptions(
            name='pocitos',
            options={'verbose_name': 'Imagen Pocitos', 'verbose_name_plural': 'Imágenes Pocitos'},
        ),
        migrations.AlterModelOptions(
            name='sanroque',
            options={'verbose_name': 'Imagen San Roque', 'verbose_name_plural': 'Imágenes San Roque'},
        ),
        migrations.AlterModelOptions(
            name='zacateros',
            options={'verbose_name': 'Imagen Zacateros', 'verbose_name_plural': 'Imágenes Zacateros'},
        ),
    ]