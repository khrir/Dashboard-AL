from django.contrib import admin
from .models import Repasses_Municipios, Despesas_Categoria_Economica, Despesas_favorecidos

@admin.register(Repasses_Municipios)
class Repasses_Municipios_Admin(admin.ModelAdmin):
    # list_display: codigo; total; nome
    list_display = ['codigo', 'total', 'nome']

@admin.register(Despesas_Categoria_Economica)
class Despesas_Categoria_Economica_Admin(admin.ModelAdmin):
    list_display = ['custeio', 'nome']

@admin.register(Despesas_favorecidos)
class Despesas_favorecidos_Admin(admin.ModelAdmin):
    list_display = ['codigo', 'total', 'nome']



