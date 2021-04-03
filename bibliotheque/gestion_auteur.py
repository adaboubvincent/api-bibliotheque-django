from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework import status



from .models import Auteur
from .serializers import AuteurSerializer



@api_view(["POST"])
def ajoutAuteur(request):
    if request.method == 'POST' :
        auteur = AuteurSerializer(data=request.data)
        if auteur.is_valid():
            auteur.save()
            return Response(auteur.data, status.HTTP_201_CREATED)
        else:
            return Response({'text': 'auteur non créé'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", 'DELETE'])
def auteur(request, id: int):
    try:
        auteur: Auteur = Auteur.objects.get(id=id)
    except Exception as e:
        return Response({'text': 'auteur non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET' :
        return Response(AuteurSerializer(auteur).data, status.HTTP_200_OK)

    elif request.method == 'PUT' :
        serializer = AuteurSerializer(auteur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'text': 'auteur non modifié'}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        auteur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def auteurs(request):
    return Response(AuteurSerializer(Auteur.objects.all(), many=True).data, status.HTTP_200_OK)