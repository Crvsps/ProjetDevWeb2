from rest_framework import serializers
from .models import Objet

class ObjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objet
        fields = ['id', 'name', 'description', 'price', 'category']