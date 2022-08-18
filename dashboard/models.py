from django.db import models

class Repasses_Municipios(models.Model):
    codigo = models.CharField(max_length=50)
    total = models.FloatField()
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome

class Despesas_Categoria_Economica(models.Model):
    custeio = models.IntegerField()
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome

class Despesas_favorecidos(models.Model):
    codigo = models.CharField(max_length=50)
    total = models.FloatField()
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome