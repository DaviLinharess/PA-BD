from django.db import models

class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clientes'       # Nome explícito da tabela no banco
        ordering = ['nome']         # Ordenação padrão nas consultas

    def __str__(self):
        return f'{self.nome} <{self.email}>'