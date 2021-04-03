from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework import status



from .models import Adherent
from .serializers import AdherentSerializer



@api_view(["POST"])
def ajoutAdherent(request):
    if request.method == 'POST' :
        adherent = AdherentSerializer(data=request.data)
        if adherent.is_valid():
            adherent.save()
            return Response(adherent.data, status.HTTP_201_CREATED)
        else:
            return Response({'text': 'adherent non créé'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", 'DELETE'])
def adherent(request, id: int):
    try:
        adherent: Adherent = Adherent.objects.get(id=id)
    except Exception as e:
        return Response({'text': 'adherent non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET' :
        return Response(AdherentSerializer(adherent).data, status.HTTP_200_OK)

    elif request.method == 'PUT' :
        serializer = AdherentSerializer(adherent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'text': 'adherent non modifié'}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        adherent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def adherents(request):
    return Response(AdherentSerializer(Adherent.objects.all(), many=True).data, status.HTTP_200_OK)