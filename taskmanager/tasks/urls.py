from django.urls import path
from . import views

urlpatterns = [
    path('',                views.index,  name='index'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('toggle/<int:pk>/', views.toggle, name='toggle'),
]