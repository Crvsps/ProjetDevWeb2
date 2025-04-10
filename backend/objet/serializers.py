from rest_framework import serializers

from .models import Category, Objet

class ObjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objet
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "status",
            "get_image",
            "get_thumbnail"
        )