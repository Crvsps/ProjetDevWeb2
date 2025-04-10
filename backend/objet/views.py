from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Objet
from .serializers import ObjetSerializer

class LatestObjectsList(APIView):
    def get(self, request, format=None):
        obj = Objet.objects.all()[0:4]
        serializer = ObjetSerializer(obj, many=True)
        return Response(serializer.data)