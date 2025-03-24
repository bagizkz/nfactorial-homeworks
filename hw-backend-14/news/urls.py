from django.urls import path
from . import views
from .views import delete_news, delete_comment

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('add/', views.news_add, name='news_add'),
    path('<int:pk>/like/', views.add_like, name='add_like'),
    path('<int:pk>/edit/', views.NewsUpdateView.as_view(), name='news_update'),
    path("news/<int:pk>/delete/", delete_news, name="delete_news"),
    path("comment/<int:pk>/delete/", delete_comment, name="delete_comment"),
]