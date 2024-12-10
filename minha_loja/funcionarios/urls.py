from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_funcionarios, name='lista_funcionarios'),
    path('adicionar/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('<int:id>/editar/', views.editar_funcionario, name='editar_funcionario'),
    path('<int:id>/excluir/', views.excluir_funcionario, name='excluir_funcionario'),
]
