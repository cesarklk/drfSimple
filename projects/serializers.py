from rest_framework import serializers
from .models import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'fecha_creacion')
        read_only_fields = ('fecha_creacion',) # la fecha de creación para que no se puede modificar.