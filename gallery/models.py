from django.db import models

class ArtWork(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    image = models.ImageField(upload_to='store', verbose_name='Imagen')
    price = models.CharField(max_length=10, verbose_name='Precio')
    technique = models.CharField(max_length=100, verbose_name = 'Técnica')
    size = models.CharField(max_length=100, verbose_name='Dimensiones')
    year = models.CharField(max_length=100, verbose_name='Año', null=True)
    url = models.URLField(max_length=200, verbose_name='Link de venta')
    order = models.SmallIntegerField(default=0, null=True, verbose_name='Orden')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'
        ordering = ['order']
    
    def __str__(self):
        return self.title