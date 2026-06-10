from django.contrib import admin
from .models import (Usuario, Atleta, Treinador, Organizador)

admin.site.register(Usuario)
admin.site.register(Atleta)
admin.site.register(Treinador)
admin.site.register(Organizador)