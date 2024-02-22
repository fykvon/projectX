from django.urls import path

from .views import (MainPage,
                    NewsView,
                    )

app_name = 'news'


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('<int:pk>/', NewsView.as_view(), name='news_number'),
]
