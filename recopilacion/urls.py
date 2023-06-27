from django.urls import path
from .views import *

urlpatterns = [
    path('respuestas/', RespuestasViews.as_view(), name='obtener-respuestas'),

]
