from rest_framework import serializers
from .models import *

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class LivreSerializer(serializers.ModelSerializer):
    ''' auteur = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nom'
     ) '''
    categorie = CategorieSerializer(many=False, read_only=True)
    auteur = AuteurSerializer(many=False, read_only=True)
    

    class Meta:
        model = Livre
        fields = '__all__'

class LivreSerializerOperation(serializers.ModelSerializer):

    class Meta:
        model = Livre
        fields = '__all__'


class AdherentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adherent
        fields = '__all__'

class BibliothequeSerializer(serializers.ModelSerializer):
    adherent = AdherentSerializer(many=False, read_only=True)
    livre = LivreSerializerOperation(many=False, read_only=True)

    class Meta:
        model = Bibliotheque
        fields = '__all__'

class BibliothequeSerializerOperation(serializers.ModelSerializer):

    class Meta:
        model = Bibliotheque
        fields = '__all__'