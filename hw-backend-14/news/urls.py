from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('add/', views.news_add, name='news_add'),
    path('<int:pk>/like/', views.add_like, name='add_like'),
]