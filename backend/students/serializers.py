from rest_framework.serializers import ModelSerializer 

from .models import Student, ObjetConnecte

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','course','grade','email','pseudo','type_membre','mot_de_passe','date_naissance','points','niveau_utilisateur','total_connexions','total_actions','date_inscription']

class ObjetConnecteSerializer(ModelSerializer):
    class Meta :
        model = ObjetConnecte
        fields = ['id','name','description','type_objet','statut','utilisateur','emplacement']