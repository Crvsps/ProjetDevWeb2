from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ObjetViewSet

router = DefaultRouter()
router.register(r'objets', ObjetViewSet)  # Cela enregistre toutes les actions par défaut

urlpatterns = [
    path('searchResultObjet/', ObjetViewSet.as_view({'get': 'list'}), name='searchResultObjet'),
    path('', include(router.urls)),  # Cela génère toutes les autres URL automatiquement
]
