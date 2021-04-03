from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework import status



from .models import Bibliotheque
from .serializers import BibliothequeSerializer, BibliothequeSerializerOperation





@api_view(["POST"])
def ajoutBibliotheque(request):
    if request.method == 'POST' :
        bibliotheque = BibliothequeSerializerOperation(data=request.data)
        if bibliotheque.is_valid():
            bibliotheque.save()
            return Response(bibliotheque.data, status.HTTP_201_CREATED)
        else:
            return Response({'text': 'bibliotheque non créé'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", 'DELETE'])
def bibliotheque(request, id: int):
    try:
        bibliotheque: Bibliotheque = Bibliotheque.objects.get(id=id)
    except Exception as e:
        return Response({'text': 'bibliotheque non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET' :
        return Response(BibliothequeSerializer(bibliotheque).data, status.HTTP_200_OK)

    elif request.method == 'PUT' :
        serializer = BibliothequeSerializerOperation(bibliotheque, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'text': 'bibliotheque non modifié'}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        bibliotheque.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def bibliotheques(request):
    return Response(BibliothequeSerializer(Bibliotheque.objects.all(), many=True).data, status.HTTP_200_OK)