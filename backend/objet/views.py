from django.db.models import Q
from django.shortcuts import render
from django.http import Http404
from django.utils.text import slugify

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Objet, Category
from .serializers import ObjetSerializer, CategorySerializer

class LatestObjectsList(APIView):    
    
    def get(self, request, format=None):
        obj = Objet.objects.all()
        serializer = ObjetSerializer(obj, many=True)
        return Response(serializer.data)
    
class ObjectDetail(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def get_object(self, category_slug, object_slug):
        try:
            return Objet.objects.filter(category__slug=category_slug).get(slug=object_slug)
        except Objet.DoesNotExist:
            raise Http404

    def get(self,request,category_slug,object_slug,format=None):
        objet = self.get_object(category_slug, object_slug)
        serializer = ObjetSerializer(objet)
        return Response(serializer.data)
    
    def put(self, request, category_slug, object_slug, format=None):
        objet = self.get_object(category_slug, object_slug)
        data = request.data.copy()
        
        if 'name' in data:
            data['slug'] = slugify(data['name'])
            
        if 'image' in request.FILES:
            objet.image = request.FILES['image']
            
        if 'image' in request.FILES or 'thumbnail' in request.FILES:
            if 'thumbnail' in request.FILES:
                objet.thumbnail = request.FILES['thumbnail']
            else:
                objet.thumbnail = objet.make_thumbnail(objet.image)
                
        if data.get('supprimer_image') == 'true':
            if objet.image:
                objet.image.delete(save=False)
            objet.image = None
            
        if data.get('supprimer_image') == 'true' or data.get('supprimer_thumbnail') == 'true':
            if data.get('supprimer_image') == 'true' and objet.image:
                objet.image.delete(save=False)
                objet.image = None

            if data.get('supprimer_thumbnail') == 'true' and objet.thumbnail:
                objet.thumbnail.delete(save=False)
                objet.thumbnail = None
        
        serializer = ObjetSerializer(objet, data=data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AddObjet(APIView):
    
    def post(self, request, format=None):
        data = request.data.copy()
        
        category_slug = data.get('category_slug')
        try:
            category = Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            return Response({"detail": "Category not found."}, status=status.HTTP_400_BAD_REQUEST)
        
        data['category'] = category.id
        
        if 'name' in data:
            data['slug'] = slugify(data['name'])

        
        if 'image' in request.FILES:
            data['image'] = request.FILES['image']
            
            if 'image' in request.FILES or 'thumbnail' in request.FILES:
                if 'thumbnail' in request.FILES:
                    data.thumbnail = request.FILES['thumbnail']
                else:
                    data.thumbnail = data.make_thumbnail(data.image)
        
        serializer = ObjetSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class DeleteObjet(APIView):
    
    def get_object(self, category_slug, object_slug):
        try:
            return Objet.objects.filter(category__slug=category_slug).get(slug=object_slug)
        except Objet.DoesNotExist:
            raise Http404
    
    def delete(self, request, category_slug, object_slug, format=None):
        objet = self.get_object(category_slug, object_slug)
        objet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   
class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
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
    
@api_view(['PUT'])
def update_objet(request, category_slug, object_slug):
    try:
        objet = Objet.objects.get(category__slug=category_slug, slug=object_slug)
    except Objet.DoesNotExist:
        return Response(status=404)
    
    data = request.data.copy()
    new_slug = slugify(data.get('name', objet.name))
    data['slug'] = new_slug
    
    serializer = ObjetSerializer(objet, data=data, partial=True)
    if serializer.is_valid():
        obj = serializer.save()
        
        if obj.slug != new_slug:
            Objet.objects.filter(id=obj.id).update(slug=new_slug)
            obj.refresh_from_db()
        
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

