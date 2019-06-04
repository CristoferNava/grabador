# Generated by Django 2.0.2 on 2019-06-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_artwork_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artwork',
            options={'ordering': ['order'], 'verbose_name': 'Obra', 'verbose_name_plural': 'Obras'},
        ),
        migrations.AddField(
            model_name='artwork',
            name='order',
            field=models.SmallIntegerField(default=0, null=True, verbose_name='Orden'),
        ),
    ]
