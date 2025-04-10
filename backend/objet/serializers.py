from rest_framework import serializers

from .models import Category, Objet


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ObjetSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Objet
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "status",
            "get_image",
            "get_thumbnail",
            "category",
            "date_added"
        )