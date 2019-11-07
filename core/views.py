from rest_framework.viewsets import ModelViewSet


from core.models import Agenda
from .serializers import AgendaSerializer


class AgendaViewSet(ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
