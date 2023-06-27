from django.urls import path

from .views import *

urlpatterns = [
    path('api/', api_home, name='api-main-view'),
    path('api/delitos/', DelitoView.as_view(), name='api-delitos'),
    path('api/delincuentes/', DelincuenteView.as_view(), name="api-delincuente")
]