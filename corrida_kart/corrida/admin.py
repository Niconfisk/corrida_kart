from django.contrib import admin
from .models import Piloto, Corrida

# Register your models here.
@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'equipe')


@admin.register(Corrida)
class CorridaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data')
