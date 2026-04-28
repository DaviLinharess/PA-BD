from rest_framework import serializers
from .models import Cliente, Vendedor, Produto

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'          # Inclui todos os campos do modelo
                                    # Para expor apenas alguns campos, use uma lista:
                                    # fields = ['id', 'nome', 'email']
                                    # Para excluir campos, use:
                                    # exclude = ['data_cadastro']

                                    
class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    categoria_display = serializers.CharField(
        source='get_categoria_display',
        read_only=True
    )

    class Meta:
        model = Produto
        fields = '__all__' # inclui categoria_display automaticamente
        extra_fields = ['categoria_display']
