from asyncio.windows_events import NULL
from pyexpat import model
from tkinter import CASCADE
from unittest.util import unorderable_list_difference
from django.db import models

# Create your models here.
class TpPessoa(models.Model):
    nome = models.CharField(max_length=50,blank=False,null=False,unique=True)

    class Meta:
        db_table = 'TpPessoa'

    def __str__(self):
        return self.nome

class CPFCNPJ(models.Model):
    valor = models.CharField(max_length=11,blank=False,null=False, unique=True)
    tipo = models.ForeignKey(TpPessoa,on_delete=models.CASCADE,blank=False,null=False)

    class Meta:
        db_table = 'CPFCNPJ'

    def __str__(self):
        return self.valor

class UF(models.Model):
    sigla = models.CharField(max_length=2,unique=True,blank=False,null=False)
    nome = models.CharField(max_length=20,unique=True,blank=False,null=False)

    class Meta:
        db_table = 'UF'

    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=50,blank=False,null=False)
    uf = models.ForeignKey(UF,on_delete=models.CASCADE,blank=False,null=False)

    class Meta:
        db_table = 'cidade'

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    SEXO = [
        ('M','Masculino'),
        ('f','Feminino'),
    ]
    CARRO = [
        ('S','Sim'),
        ('N','Não'),
    ]
    ESTADO_CIVIL = [
        (1,'Solteiro(a)'),
        (2,'Casado(a)'),
        (3,'Divorciado(a)'),
        (4,'Viúvo(a)'),
        (5,'Desquitado(a)'),
        (6,'União Estável'),
    ]
    FILHOS = [
        ('S','Sim'),
        ('N','Não'),
    ]
    nome = models.CharField(max_length=50,null=False,blank=False)
    email = models.CharField(max_length=100,null=True,blank=True)
    nasc = models.DateField(null=True,blank=True)
    cpfcnpj = models.OneToOneField(CPFCNPJ,on_delete=models.CASCADE,blank=False,null=False)
    cidade = models.ManyToManyField(Cidade)
    sexo = models.CharField(max_length=1,choices=SEXO, null=True,blank=True)
    profissao = models.CharField(max_length=50,null=True,blank=True)
    renda = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    carro = models.CharField(max_length=1,choices=CARRO,null=True,blank=True)
    EstCivil = models.IntegerField(choices=ESTADO_CIVIL,default=1,null=True,blank=True)
    filhos = models.CharField(max_length=1,choices=FILHOS,null=True,blank=True)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nome


