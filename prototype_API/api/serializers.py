from rest_framework import serializers

from ..models import *


class DelincuenteSerializer(serializers.ModelSerializer):
    model = Delincuente
    fields = "__all__"


class VictimaSerializer(serializers.ModelSerializer):
    model = Victima
    fields = "__all__"


class OficialSerializer(serializers.ModelSerializer):
    model = Oficial
    fields = "__all__"


class TestigoSerializer(serializers.ModelSerializer):
    model = Testigo
    fields = "__all__"


class DelitoSerializer(serializers.ModelSerializer):
    model = Delito
    fields = "__all__"


class PruebasDelitoSerializer(serializers.ModelSerializer):
    model = PruebasDelito
    fields = "__all__"
