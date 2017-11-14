from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    nome = models.CharField(max_length=128)
    cod = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    idade = models.IntegerField()
    nomeChef = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Frequencia(models.Model):
    ES = (
        (1, "Entrada"),
        (2, "Saída"),
    )
    entrada_Saida = models.CharField(max_length=1, choices=ES)
    confg = (
        (1, "08:00/13:00"),
        (2, "08:00/12:00 e 14:00/18:00"),
    )
    configuraçãoHora = models.CharField(max_length=1, choices=confg)
    dataEHora = models.DateTimeField(blank=True, null=True)
    consistente = models.BooleanField('Consistente')
    ip = models.CharField(max_length=50)
    funcionario = models.ForeignKey(Funcionario, null=True, blank=False)

    def __str__(self):
        return self.consistente

class Justificativa(models.Model):
    justificativa = models.TextField(max_length=200)
    funcionario = models.ForeignKey(Funcionario, null=True, blank=False)

    def __str__(self):
        return self.justificativa
