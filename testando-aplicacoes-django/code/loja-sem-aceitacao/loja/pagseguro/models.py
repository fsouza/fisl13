from django.contrib.auth import models as auth_models
from django.db import models


class Pedido(models.Model):
    usuario = models.ForeignKey(auth_models.User)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super(Pedido, self).__init__(*args, **kwargs)
        self._itens = []
        self.valor = 0

    def adicionar_item(self, produto):
        self._itens.append(Item(nome=produto.nome, preco=produto.preco, pedido=self))
        self.valor += produto.preco

    def save(self, *args, **kwargs):
        super(Pedido, self).save(*args, **kwargs)
        for item in self._itens:
            item.pedido = self
            item.save()


class Item(models.Model):
    nome = models.CharField(max_length=500)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    pedido = models.ForeignKey(Pedido)
