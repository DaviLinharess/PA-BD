from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):

    class Tipo(models.TextChoices):
        ATLETA = 'ATLETA', 'Atleta'
        TREINADOR = 'TREINADOR', 'Treinador'
        ORGANIZADOR = 'ORGANIZADOR', 'Organizador'

    tipo = models.CharField(max_length=12, choices=Tipo.choices, default=Tipo.ATLETA)

    data_nasc = models.DateField(null=True, blank=True)

    cidade = models.CharField(max_length=80,blank=True)

    def is_atleta(self):
        return self.tipo == self.Tipo.ATLETA

    def is_treinador(self):
        return self.tipo == self.Tipo.TREINADOR

    def is_organizador(self):
        return self.tipo == self.Tipo.ORGANIZADOR

    def __str__(self):
        return f'{self.username} ({self.get_tipo_display()})'


class Atleta(models.Model):

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_atleta')

    cpf = models.CharField(max_length=11, unique=True)

    categoria = models.CharField(max_length=10,choices=[
            ('5K', '5K'),
            ('10K', '10K'),
            ('21K', '21K'),
            ('42K', '42K')
        ],default='10K'
    )

    melhor_tempo = models.DurationField(null=True,blank=True)

    def __str__(self):
        return f'Atleta: {self.usuario.username} ({self.categoria})'


class Treinador(models.Model):

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_treinador')

    cref = models.CharField(max_length=20, unique=True)

    especialidade = models.CharField(max_length=60,blank=True)

    qtd_atletas_max = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f'Treinador: {self.usuario.username} (CREF {self.cref})'


class Organizador(models.Model):

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_organizador')

    cnpj = models.CharField(max_length=14, unique=True)

    nome_organizacao = models.CharField(max_length=120)

    uf = models.CharField(max_length=2)

    def __str__(self):
        return f'Org: {self.nome_organizacao} ({self.uf})'