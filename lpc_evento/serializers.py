from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from lpc_evento.models import *

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

    def create(self, dados):
        return Funcionario.objects.create(**dados)

class FrequenciaSerializer(serializers.HyperlinkedModelSerializer):
    funcionario = FuncionarioSerializer(many = False)
    class Meta:
        model = Frequencia
        fields = '__all__'

    def create(self, dados):
        funcionario_data = validated_data.pop('funcionario')
        f = Funcionario.objects.create(**funcionario_data)
        fe = Frequencia.objects.create(funcionario = f, **validated_data)
        return fe


class JustificativaSerializer(serializers.HyperlinkedModelSerializer):
    funcionario = FuncionarioSerializer(many = False)
    class Meta:
        model = Justificativa
        fields = '__all__'

    def create(self, dados):
        funcionario_data = validated_data.pop('funcionario')
        f = Funcionario.objects.get(nome = funcionario_data)
        j = Justificativa.objects.create(funcionario = f, **validated_data)
        return j
