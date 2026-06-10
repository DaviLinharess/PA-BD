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

        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "tipo": request.user.tipo,
            "cidade": request.user.cidade
        })

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