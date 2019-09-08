from django.db import models

class Pocitos(models.Model):
    image1 = models.ImageField(upload_to='points', verbose_name='Imagen 1')
    image2 = models.ImageField(blank=True, null=True, upload_to='points', verbose_name='Imagen 2 (opcional)')
    image3 = models.ImageField(blank=True, null=True, upload_to='points', verbose_name='Imagen 2 (opcional)')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    class Meta:
        verbose_name = 'Imagen Pocitos'
        verbose_name_plural = 'Imágenes Pocitos'

    def __str__(self):
        return "Imágenes Pocitos"

class SanRoque(models.Model):
    image1 = models.ImageField(upload_to='points', verbose_name='Imagen 1')
    image2 = models.ImageField(blank=True, null=True, upload_to='points', verbose_name='Imagen 2 (opcional)')
    image3 = models.ImageField(blank=True, null=True, upload_to='points', verbose_name='Imagen 2 (opcional)')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    class Meta:
        verbose_name = 'Imagen San Roque'
        verbose_name_plural = 'Imágenes San Roque'

    def __str__(self):
        return "Imágenes San Roque"

class Zacateros(models.Model):
    image1 = models.ImageField(upload_to='points', verbose_name='Imagen 1')
    image2 = models.ImageField(blank=True, null=True, upload_to='points', verbose_name='Imagen 2 (opcional)')
    image3 = models.ImageField(blank=True, null=True, upload_to='points', verbose_name='Imagen 2 (opcional)')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    class Meta:
        verbose_name = 'Imagen Zacateros'
        verbose_name_plural = 'Imágenes Zacateros'

    def __str__(self):
        return "Imágenes Zacateros"

class Oaxaca(models.Model):
    image1 = models.ImageField(upload_to='points', verbose_name='Imagen 1')
    image2 = models.ImageField(blank=True, null=True, upload_to='points', verbose_name='Imagen 2 (opcional)')
    image3 = models.ImageField(blank=True, null=True, upload_to='points', verbose_name='Imagen 2 (opcional)')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    class Meta:
        verbose_name = 'Imagen Oaxaca'
        verbose_name_plural = 'Imágenes Oaxaca'

    def __str__(self):
        return "Imágenes Oaxaca"