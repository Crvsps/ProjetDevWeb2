from rest_framework import viewsets
from rest_framework.response import Response
from .models import Objet
from .serializers import ObjetSerializer
from django_filters import rest_framework as filters

class ObjetFilter(filters.FilterSet):
    # Exemple de filtre
    name = filters.CharFilter(lookup_expr='icontains')  # Filtrer par nom
    category = filters.CharFilter(lookup_expr='icontains')  # Filtrer par catégorie

    class Meta:
        model = Objet
        fields = ['name', 'category']  # Tu peux ajouter d'autres champs pour le filtrage

class ObjetViewSet(viewsets.ModelViewSet):
    queryset = Objet.objects.all()
    serializer_class = ObjetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ObjetFilter

    # La méthode list est automatiquement utilisée par le router pour les requêtes GET
    def list(self, request, *args, **kwargs):
        # Ce code permet de filtrer les objets selon les critères de recherche
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
