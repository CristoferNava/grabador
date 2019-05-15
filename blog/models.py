from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    image = models.ImageField(upload_to='blog', verbose_name='Portada')
    short_description = RichTextField(verbose_name='Descripción corta')
    content = RichTextField(verbose_name='Contenido')
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