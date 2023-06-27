from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class EncuestaViews(APIView):
    def get(self, request):
        pregunta = Preguntas.objects.all()
        serializer = PreguntaSerializers(pregunta, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PreguntaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PreguntasViews(APIView):
    def get(self, request):
        pregunta = Preguntas.objects.all()
        serializer = PreguntaSerializers(pregunta, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PreguntaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PreguntasDetails(APIView):
    def get_object(self, pk):
        try:
            return Preguntas.objects.get(id=pk)
        except Preguntas.DoesNotExit:
            raise Http404

    def get(self, pk):
        pregunta = self.get_object(pk)
        serializer = PreguntaSerializers(pregunta)
        return Response(serializer.data)


class RespuestasViews(APIView):
    def get(self, request):
        respuestas = Respuestas.objects.all()
        serializer = RespuestaSerializers(respuestas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RespuestaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
