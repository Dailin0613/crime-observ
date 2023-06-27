from django.contrib import admin
from .models import Preguntas, Respuestas, Encuestas

admin.site.register(Encuestas)
admin.site.register(Preguntas)
admin.site.register(Respuestas)

