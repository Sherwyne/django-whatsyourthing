from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('registrants/', views.registrants, name='registrants'),
    path('create/', views.create, name='create'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    
    
    
]