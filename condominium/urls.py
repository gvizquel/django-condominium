"""condominium URL Configuration
"""
# Librerias Django
from django.conf import settings
from django.conf.urls import handler404, handler500, include
from django.contrib import admin
from django.urls import path
from django.views.static import serve


urlpatterns = [
    path('account/', include('apps.usercustom.urls')),
    path('admin/', admin.site.urls),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT, }),
]


handler404 = 'apps.usercustom.views.error_404'
handler500 = 'apps.usercustom.views.error_500'
