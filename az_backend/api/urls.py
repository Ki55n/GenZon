from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from api import views

urlpatterns = [
    path('register', views.UserRegisterView.as_view(), name='user-register'),
    path('login', views.UserLoginView.as_view(), name='user-login'),
    path('refresh-token', TokenRefreshView.as_view(), name="refresh-token"),

    path('profile', views)
]
