from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='colinhas'),
    path('editar/<int:pk>/', views.editar, name='editar_colinha'),
    path('excluir/<int:pk>/', views.excluir, name='excluir_colinha'),
    path('favorito/<int:pk>/', views.toggle_favorito, name='toggle_favorito'),
    path('reordenar/', views.reordenar, name='reordenar_colinhas'),
]