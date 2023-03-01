from django.shortcuts import render
from rest_framework import viewsets
from api_app.models import Usuarios
from api_app.serializers import UsuariosSerializer

# Create your views here.

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
