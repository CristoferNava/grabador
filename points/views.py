from django.shortcuts import render
from .models import Pocitos, SanRoque, Zacateros, Oaxaca

def points(request):
    pocitos = Pocitos.objects.all()
    san_roque = SanRoque.objects.all()
    zacateros = Zacateros.objects.all()
    oaxaca = Oaxaca.objects.all()

    return render(request, 'points/points.html',
        {'pocitos': pocitos, 
         'san_roque': san_roque, 
         'zacateros': zacateros,
         'oaxaca': oaxaca})