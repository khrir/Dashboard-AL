from django.urls import path 

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("relatorio_repasses_municipios", views.relatorio_repasses_municipios, name="relatorio_repasses_municipios"),
    path("relatorio_despesas_categoria_economica", views.relatorio_despesas_categoria_economica, name="relatorio_despesas_categoria_economica"),
    path("relatorio_despesas_favorecidos", views.relatorio_despesas_favorecidos, name="relatorio_despesas_favorecidos")
]
