from django.db.models import Q
from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Objet
from .serializers import ObjetSerializer

class LatestObjectsList(APIView):
    def get(self, request, format=None):
        obj = Objet.objects.all()[0:4]
        serializer = ObjetSerializer(obj, many=True)
        return Response(serializer.data)
    
class ObjectDetail(APIView):
    def get_object(self, category_slug, object_slug):
        try:
            return Objet.objects.filter(category__slug=category_slug).get(slug=object_slug)
        except Objet.DoesNotExist:
            raise Http404

    def get(self,request,category_slug,object_slug,format=None):
        objet = self.get_object(category_slug, object_slug)
        serializer = ObjetSerializer(objet)
        return Response(serializer.data)
    
@api_view(['POST'])
def search(request):
    query = request.data.get('query','')
    
    if query:
        objects = Objet.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ObjetSerializer(objects,many=True)
        return Response(serializer.data)
    else:
        return Response({"objects": []})