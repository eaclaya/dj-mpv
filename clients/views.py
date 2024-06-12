from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def client_list(request):
    if domain := request.GET.get('domain', None):
        try:
            client = Client.objects.get(domain=domain)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        except Client.DoesNotExist as e:
            raise NotFound('Client not found') from e
    else:
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def client_detail(request, pk):
    try:
        client = Client.objects.get(id=pk)
    except Client.DoesNotExist as e:
        raise NotFound('Client not found') from e

    serializer = ClientSerializer(client)
    return Response(serializer.data)
