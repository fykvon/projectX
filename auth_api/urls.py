from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import ProfileLoginView, ProfileLogoutView


app_name = 'auth_api'

urlpatterns = [
    path('login/', ProfileLoginView.as_view(), name='login'),
    path('logout/', ProfileLogoutView.as_view(), name='logout'),
]
