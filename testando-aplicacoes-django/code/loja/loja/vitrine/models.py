from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=500)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
