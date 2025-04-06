from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # 🔎 Campos para filtrar diretamente via ?campo=valor
    filterset_fields = ['categoria', 'ativo']
    
    # 🔍 Busca por texto livre
    search_fields = ['nome', 'descricao']
    
    # ↕️ Ordenação por qualquer campo (ex: ?ordering=preco ou ?ordering=-estoque)
    ordering_fields = ['preco', 'estoque', 'criado_em']





#v1.1
from rest_framework import viewsets
from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
