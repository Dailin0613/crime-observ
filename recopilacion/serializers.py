from rest_framework import serializers
from .models import Encuestas, Respuestas, Preguntas


class EncuestaSerializers(serializers.Serializer):
    class Meta:
        model = Encuestas
        fields = '__all__'


class RespuestaSerializers(serializers.Serializer):
    class Meta:
        model = Respuestas
        fields = '__all__'


class PreguntaSerializers(serializers.Serializer):
    class Meta:
        model = Preguntas
        fields = '__all__'
