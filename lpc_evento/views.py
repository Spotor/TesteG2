from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.http import HttpResponse
from lpc_evento.models import *
from lpc_evento.serializers import *

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class JustificativaViewSet(viewsets.ModelViewSet):
    queryset = Justificativa.objects.all()
    serializer_class = JustificativaSerializer
