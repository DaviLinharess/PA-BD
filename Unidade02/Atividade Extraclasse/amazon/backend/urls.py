
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend import views 

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename='cliente')
router.register(r'vendedores', views.VendedorViewSet, basename='vendedor') 
router.register(r'produtos', views.ProdutoViewSet, basename='produto') 
router.register(r'perfis-vendedores', views.PerfilVendedorViewSet, basename='perfil-vendedor') # NOVO
router.register(r'pedidos', views.PedidoViewSet, basename='pedido') # NOVO
router.register(r'itens-pedido', views.ItemPedidoViewSet, basename='item-pedido') #NOVO

urlpatterns = [
    path('', include(router.urls)),
]