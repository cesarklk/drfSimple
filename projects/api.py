from .models import Proyecto
from rest_framework  import viewsets, permissions
from .serializers import ProyectoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    permissions = [permissions.AllowAny]
    serializer_class = ProyectoSerializer