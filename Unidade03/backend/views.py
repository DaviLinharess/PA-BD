from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Usuario
from .serializers import (
    UsuarioSerializer,
    LoginSerializer
)

from .permissions import (
    IsAtleta,
    IsTreinador,
    IsOrganizador
)

class SignupView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = UsuarioSerializer(data=request.data)

        if serializer.is_valid():

            usuario = serializer.save()

            return Response(
                UsuarioSerializer(usuario).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class PerfilView(APIView):

    def get(self, request):

        usuario = request.user

        dados = {
            "id": usuario.id,
            "username": usuario.username,
            "email": usuario.email,
            "tipo": usuario.tipo,
            "cidade": usuario.cidade
        }

        if (
            usuario.is_atleta()
            and hasattr(usuario, 'perfil_atleta')
        ):
            dados["perfil_atleta"] = {
                "cpf": usuario.perfil_atleta.cpf,
                "categoria": usuario.perfil_atleta.categoria,
                "melhor_tempo": usuario.perfil_atleta.melhor_tempo
            }

        elif (
            usuario.is_treinador()
            and hasattr(usuario, 'perfil_treinador')
        ):
            dados["perfil_treinador"] = {
                "cref": usuario.perfil_treinador.cref,
                "especialidade": usuario.perfil_treinador.especialidade,
                "qtd_atletas_max": usuario.perfil_treinador.qtd_atletas_max
            }

        elif (
            usuario.is_organizador()
            and hasattr(usuario, 'perfil_organizador')
        ):
            dados["perfil_organizador"] = {
                "cnpj": usuario.perfil_organizador.cnpj,
                "nome_organizacao": usuario.perfil_organizador.nome_organizacao,
                "uf": usuario.perfil_organizador.uf
            }

        return Response(dados)

class TreinoView(APIView):

    permission_classes = [IsAtleta]

    def post(self, request):

        return Response({
            "mensagem": "Treino registrado com sucesso.",
            "dados": request.data
        })

class AtletasView(APIView):

    permission_classes = [IsTreinador]

    def get(self, request):

        return Response({
            "mensagem": "Lista de atletas orientados."
        })

class EventoView(APIView):

    permission_classes = [IsOrganizador]

    def post(self, request):

        return Response({
            "mensagem": "Evento criado com sucesso.",
            "evento": request.data
        })