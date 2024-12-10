from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fornecedores, name='lista_fornecedores'),
    path('adicionar/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('<int:id>/editar/', views.editar_fornecedor, name='editar_fornecedor'),
    path('<int:id>/excluir/', views.excluir_fornecedor, name='excluir_fornecedor'),
]
