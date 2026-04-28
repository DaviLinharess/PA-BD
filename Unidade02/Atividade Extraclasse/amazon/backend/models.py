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


class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    avaliacao = models.DecimalField(max_digits=3, decimal_places=2, default=5.00)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'vendedores'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.cpf_cnpj})'



class Produto(models.Model):
    CATEGORIA_CHOICES = [
        ('eletronicos', 'Eletrônicos'),
        ('roupas', 'Roupas e Acessórios'),
        ('livros', 'Livros'),
        ('alimentos', 'Alimentos'),
        ('outros', 'Outros'),
    ]

    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='outros')
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'produtos'
        ordering = ['nome']

    def __str__(self):
        return f'[{self.nome} — R$ {self.preco}'


class PerfilVendedor(models.Model):
    vendedor = models.OneToOneField(
        Vendedor,
        on_delete=models.CASCADE,
        related_name='perfil',
        primary_key=True            # usa o id do vendedor como PK
    )
    razao_social = models.CharField(max_length=150, blank=True)
    inscricao_estadual = models.CharField(max_length=20, blank=True)
    banco = models.CharField(max_length=50, blank=True)
    agencia = models.CharField(max_length=10, blank=True)
    conta = models.CharField(max_length=20, blank=True)
    chave_pix = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'perfis_vendedores'

    def __str__(self):
        return f'Perfil de {self.vendedor.nome}'

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT, # cliente com pedidos não pode ser apagado
        related_name='pedidos'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )
    data_pedido = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True)

    class Meta:
        db_table = 'pedidos'
        ordering = ['-data_pedido']

    def __str__(self):
        return f'Pedido #{self.id} — {self.cliente.nome}'

class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE, # itens não existem sem o pedido
        related_name='itens'
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT, # produto com vendas não pode ser apagado
        related_name='itens_vendidos'
    )

    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Preço congelado no momento da compra'
    )

    class Meta:
        db_table = 'itens_pedido'
        unique_together = ['pedido', 'produto'] # mesmo produto não duplica no pedido

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome}'

    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario
