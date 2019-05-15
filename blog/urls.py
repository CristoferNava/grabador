from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.blog, name='blog'), 
    path('<int:article_id>/<slug:article_slug>/', blog_views.article, name='article'),
]