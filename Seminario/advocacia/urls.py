from django.urls import path, include
from . import views  # Aqui você importa a view home
from rest_framework.routers import DefaultRouter
from advogados.views import AdvogadoViewSet
from django.shortcuts import render
from django.contrib import admin
from django.urls import path

def home(request):
    return render(request, 'home.html')




router = DefaultRouter()
router.register(r'advogados', AdvogadoViewSet, basename='advogado')
urlpatterns = [
    
    path('api/', include(router.urls)),  # Incluindo as rotas da API de advogados
    path('', views.home, name='home'),  # Página inicial
    path('', include('advogados.urls')),
    path('', home, name='home'),
    path('', views.home, name='home'),
    path('', include('advogados.urls')),
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    