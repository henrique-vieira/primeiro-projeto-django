from django.db import models


class Funcionario(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    tempo_de_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

    objetos = models.Manager()

class Curriculo(models.Model):
    SEXO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
    )

    ESTADO_CIVIL_CHOICES = (
        ('S', u'Solteiro'),
        ('C', u'Casado'),
        ('D', u'Divorciado'),
        ('V', u'Viúvo'),
    )
    nome = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    cpf = models.CharField(
        max_length=14,
        null=True,
        blank=True
    )

    TelCelular = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        verbose_name='Nº telefone celular'
    )
    TelFixo = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        verbose_name='Nº telefone fixo'
    )
    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES
    )
    estado_civil = models.CharField(
        max_length=1,
        choices=ESTADO_CIVIL_CHOICES,
        verbose_name='Estado civil'
    )
    email = models.EmailField(
        null=True
    )
    idade = models.IntegerField(
        blank=True,
        null=True
    )
    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    login = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    rua =  models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    numero = models.IntegerField(
        blank=True,
        null=True
    )
    bairro = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    cidade  =  models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    estado  =  models.CharField(
        max_length=2,
        null=True,
        blank=True
    )
    cep = models.CharField(
        max_length=9,
        blank=True,
        null=True
    )
    curriculo = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    descricao = models.TextField()

    criadoData = models.DateTimeField()

    status = models.IntegerField(
        blank=True,
        null=True
    )

    objetos = models.Manager()