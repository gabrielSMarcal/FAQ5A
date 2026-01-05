from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topico_id>/', views.index, name='index_com_id'),
    path('adicionar/', views.adicionar, name='adicionar'),
]