from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('entradagrabador/', admin.site.urls),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('form/', include('form.urls')),
    path('gallery/', include('gallery.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'El Pinche Grabador'
admin.site.index_title = 'Sitio Administrativo'
admin.site.site_title = 'El Pinche Grabador'