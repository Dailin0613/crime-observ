from django.urls import path
from .views.main__view import home

urlpatterns = [
    path('', home, name='main-view')
]
