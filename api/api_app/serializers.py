from rest_framework import serializers
from api_app.models import Usuarios

class UsuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Usuarios
        fields = ['usuario_id','full_name', 'birthdate', 'email', 'profile_img', 'usuario_id']