from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='colinhas'),
    path('editar/<int:pk>/', views.editar, name='editar_colinha'),
    path('excluir/<int:pk>/', views.excluir, name='excluir_colinha'),
]