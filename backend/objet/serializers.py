from rest_framework import serializers

from .models import Category, Objet


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ObjetSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Objet
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url",
            "description",
            "status",
            "get_image",
            "get_thumbnail",
            "category",
            "date_added",
            "marque",
            "consommation",
            "localisation",
            "derniere_maintenance",
        )