from django.shortcuts import render
from gallery.models import ArtWork
from blog.models import Article

def about(request):
    return render(request, 'core/about.html')
    
def home(request):
    pictures = ArtWork.objects.all()
    articles = Article.objects.all()
    return render(request, 'core/index.html', {'pictures': pictures, 'articles': articles})

def points(request):
    return render(request, 'core/puntos.html')

def store(request):
    return render(request, 'core/store.html')

def taller(request):
    return render(request, 'core/taller.html')
