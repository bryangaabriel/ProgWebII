from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_advogados, name='listar_advogados'),
    path('adicionar/', views.adicionar_advogado, name='adicionar_advogado'),
    path('editar/<int:pk>/', views.editar_advogado, name='editar_advogado'),
    path('excluir/<int:pk>/', views.excluir_advogado, name='excluir_advogado'),
    path('list/', views.listar_advogados, name='list_advogados'),
]