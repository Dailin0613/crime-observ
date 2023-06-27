from django.urls import path

# token view
from rest_framework_simplejwt.views import (TokenRefreshView)

from .views import *
from .views import MyTokenObtainPairView

urlpatterns = [
    path('api/token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('signin', Signin, name='signin'),
    path('signup', Signup, name='signup'),
    path('logout', Logout, name='logout'),
    path('update', UpdateUserData, name='user-update-data')
]
