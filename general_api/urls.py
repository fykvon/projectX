from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from .views import (CreatePlayerView,
                    UpdateUserView,
                    DeleteUserView,
                    DetailUserView,
                    PlayerViewSet,
                    DivisionView,
                    DivisionDetailView,
                    PlayerDetailView,
                    TeamDetailView,
                    )

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)

app_name = 'general_api'

urlpatterns = [
    path('create/', CreatePlayerView.as_view(), name='create_player'),
    path('update/', UpdateUserView.as_view(), name='update_player'),
    path('delete/', DeleteUserView.as_view(), name='delete_player'),
    path('detail/', DetailUserView.as_view(), name='detail_player'),
    path('divisions/', DivisionView.as_view(), name='divisions'),
    path('divisions/<int:pk>/', DivisionDetailView.as_view(), name='division_detail'),
    path('player/<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),
    path('team/<str:slug>', TeamDetailView.as_view(), name='team_detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
