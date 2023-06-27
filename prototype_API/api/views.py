from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .serializers import *


@api_view('GET')
def api_home():
    delitos = Delito.objects.all()
    serializer = DelitoSerializer(delitos, many=True)
    return Response(serializer.data)


class DelitoView(generics.ListAPIView):
    queryset = Delito.objects.all()
    serializer_class = DelitoSerializer


class DelincuenteView(generics.ListAPIView):
    queryset = Delincuente.objects.all()
    serializer_class = DelincuenteSerializer


class VictimaView(generics.ListAPIView):
    queryset = Victima.objects,all()
    serializer_class = VictimaSerializer
