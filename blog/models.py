from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    image = models.ImageField(upload_to='blog', verbose_name='Portada')
    short_description = RichTextField(max_length=45, verbose_name='Descripción corta')
    first_paragraph = RichTextField(verbose_name='Contenido', null=True)
    first_image = models.ImageField(upload_to='blog', blank=True, null=True, verbose_name='Primer imagen (opcional)')
    second_paragraph = RichTextField(null=True, blank=True, verbose_name='Segundo párrafo (opcional)')
    second_image = models.ImageField(upload_to='blog', blank=True, null=True, verbose_name='Segunda imagen (opcional)')
    third_paragraph = RichTextField(null=True, blank=True, verbose_name='Tercer párrafo (opcional)')
    third_image = models.ImageField(upload_to='blog', blank=True, null=True, verbose_name='Tercera imagen imagen (opcional)')
    day = models.CharField(max_length=2, verbose_name='Día')
    month = models.CharField(max_length=15, verbose_name='Mes')
    author = models.CharField(max_length=100, verbose_name='Autor')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['-created']

    def __str__(self):
        return self.title