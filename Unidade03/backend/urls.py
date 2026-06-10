from django.urls import path

from .views import (SignupView, LoginView, PerfilView, TreinoView, AtletasView, EventoView)

from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [

    path('signup/', SignupView.as_view()),

    path('login/', LoginView.as_view()),

    path('refresh/', TokenRefreshView.as_view()),

    path('perfil/', PerfilView.as_view()),

    path('treino/', TreinoView.as_view()),

    path('atletas/', AtletasView.as_view()),

    path('evento/', EventoView.as_view()),
]