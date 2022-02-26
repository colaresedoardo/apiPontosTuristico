from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from core.models import Atracao
from .serializers import AtracoesSerializer

class AtracaoViewSet(ModelViewSet):

    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nome',)