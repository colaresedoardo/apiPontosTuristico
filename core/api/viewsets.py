from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristicos
from .serializers import PontoTuristicosSerializer

class PontoTuristicosViewSet(ModelViewSet):


    serializer_class = PontoTuristicosSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ('descricao',)


    def get_queryset(self):
        id = self.request.query_params.get("id", None)
        nome = self.request.query_params.get("nome", None)
        descricao = self.request.query_params.get("descricao", None)

        queryset = PontoTuristicos.objects.all()
        if id:
            queryset = PontoTuristicos.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(nome__icontains=descricao)

        return queryset


#    def list(self, request, *args, **kwargs):
#        return Response({'test:12'})

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicos,self).create(request, *args, **kwargs)

#    @action(methods=['get'], detail=True)
#    def denuciar(self, request, pk=None):
#        pass