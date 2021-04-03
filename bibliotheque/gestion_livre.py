from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework import status



from .models import Livre
from .serializers import LivreSerializer, LivreSerializerOperation





@api_view(["POST"])
def ajoutLivre(request):
    if request.method == 'POST' :
        livre = LivreSerializerOperation(data=request.data)
        print(livre.is_valid())
        if livre.is_valid():
            livre.save()
            return Response(livre.data, status.HTTP_201_CREATED)
        else:
            return Response({'text': 'livre non créé'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", 'DELETE'])
def livre(request, id: int):
    try:
        livre: Livre = Livre.objects.get(id=id)
    except Exception as e:
        return Response({'text': 'livre non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET' :
        return Response(LivreSerializer(livre).data, status.HTTP_200_OK)

    elif request.method == 'PUT' :
        serializer = LivreSerializerOperation(livre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'text': 'livre non modifié'}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        livre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def livres(request):
    return Response(LivreSerializer(Livre.objects.all(), many=True).data, status.HTTP_200_OK)