from django.urls import path
from . import views as core_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('web/', core_views.home, name='web'),
    path('about/', core_views.about, name='about'),
    path('store/', core_views.store, name='store'),
    path('taller/', core_views.taller, name='taller'),
]