from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristicos
from atracoes.api.serializers import AtracoesSerializer
class PontoTuristicosSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    nome_descricao = SerializerMethodField()
    class Meta:
        model = PontoTuristicos

        fields = ['id', 'nome_descricao','nome','id_descricao', 'descricao','aprovado', 'fotos','atracoes']


    def get_nome_descricao(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
