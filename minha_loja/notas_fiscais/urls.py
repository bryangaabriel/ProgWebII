from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notas_fiscais, name='lista_notas_fiscais'),
    path('adicionar/', views.adicionar_nota_fiscal, name='adicionar_nota_fiscal'),
    path('<int:id>/editar/', views.editar_nota_fiscal, name='editar_nota_fiscal'),
    path('<int:id>/excluir/', views.excluir_nota_fiscal, name='excluir_nota_fiscal'),
    path('<int:id>/detalhes/', views.detalhes_nota_fiscal, name='detalhes_nota_fiscal'),
]
