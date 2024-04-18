from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import ProfileLoginView, ProfileLogoutView, ProfileRegisterView, ThanksView

app_name = 'auth_api'

urlpatterns = [
    path('login/', ProfileLoginView.as_view(), name='login'),
    path('logout/', ProfileLogoutView.as_view(), name='logout'),
    path('register/', ProfileRegisterView.as_view(), name='register'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
]
