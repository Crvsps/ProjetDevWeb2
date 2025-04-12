from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('auth.urls')),
    path('api/v1/users/',include('users.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('objets/', include('objet.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
