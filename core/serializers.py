from rest_framework.serializers import ModelSerializer
from core.models import Agenda


class AgendaSerializer(ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'local', 'data', 'horario', 'valor',
                  'responsavel', 'contato')
