from django.urls import path
from . import views as gallery_views

urlpatterns = [
    path('', gallery_views.gallery, name='gallery'),
    path('<int:picture_id>/<slug:picture_slug>/', gallery_views.picture, name='picture'),
]