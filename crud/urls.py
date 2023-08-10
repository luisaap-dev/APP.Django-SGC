from django.contrib import admin
from django.urls import path
from crudpy import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('añadir_cliente/', views.añadir_cliente, name='añadir_cliente'),
    path('detalle_cliente/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
