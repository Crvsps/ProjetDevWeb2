from rest_framework import serializers

from .models import Category, Objet


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ObjetSerializer(serializers.ModelSerializer):
    
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_detail = CategorySerializer(source='category', read_only=True)
    
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
            "category_detail",
            "date_added",
            "marque",
            "consommation",
            "localisation",
            "derniere_maintenance",
        )