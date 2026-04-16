from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend import views 

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename='cliente')

urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('amazon_api/', include(routers.urls)),    # Todos os endpoints da API

]
