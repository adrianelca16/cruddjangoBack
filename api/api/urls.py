
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_app.views import UsuariosViewSet


router = routers.DefaultRouter()
router.register(r'usuario', UsuariosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
