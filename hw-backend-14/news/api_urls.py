from django.urls import path
from .views import NewsListCreateAPIView, NewsDetailAPIView

urlpatterns = [
    path('', NewsListCreateAPIView.as_view(), name='news-list-create'),
    path('<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
]