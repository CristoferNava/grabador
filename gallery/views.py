from django.shortcuts import get_object_or_404, render
from .models import ArtWork

def gallery(request):
    pictures = ArtWork.objects.all()
    return render(request, 'gallery/galeria.html', {'pictures': pictures})

def picture(request, picture_id, picture_slug):
    picture = get_object_or_404(ArtWork, id=picture_id)
    return render(request, 'gallery/store.html', {'picture': picture})
