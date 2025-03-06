from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_nfactorial),
    path('<int:first>/add/<int:second>/', views.add),
    path('transform/<str:text>/', views.upper),
    path('check/<str:word>/', views.palindrome),
    path('calc/<int:first>/<str:operation>/<int:second>/', views.calculator),
]