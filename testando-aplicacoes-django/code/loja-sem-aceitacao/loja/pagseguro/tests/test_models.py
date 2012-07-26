# -*- coding: utf-8 -*-
from django import test
from django.contrib.auth import models as auth_models
from django.db import models as django_models

from loja.pagseguro import models
from loja.vitrine import models as vitrine_models


class ItemTestCase(test.TestCase):

    def test_item_deve_ter_nome(self):
        fields = models.Item._meta.get_all_field_names()
        self.assertIn("nome", fields)

    def test_nome_deve_ser_charfield(self):
        field = models.Item._meta.get_field_by_name("nome")[0]
        self.assertIsInstance(field, django_models.CharField)

    def test_nome_deve_ter_no_maximo_500_caracteres(self):
        field = models.Item._meta.get_field_by_name("nome")[0]
        self.assertEqual(500, field.max_length)

    def test_item_deve_ter_preco(self):
        fields = models.Item._meta.get_all_field_names()
        self.assertIn("preco", fields)

    def test_preco_deve_ser_decimalfield(self):
        field = models.Item._meta.get_field_by_name("preco")[0]
        self.assertIsInstance(field, django_models.DecimalField)

    def test_preco_deve_ter_no_maximo_10_digitos(self):
        field = models.Item._meta.get_field_by_name("preco")[0]
        self.assertEqual(10, field.max_digits)

    def test_preco_deve_ter_duas_casas_decimais(self):
        field = models.Item._meta.get_field_by_name("preco")[0]
        self.assertEqual(2, field.decimal_places)

    def test_item_deve_ter_referencia_para_pedido(self):
        field = models.Item._meta.get_field_by_name("pedido")[0]
        self.assertIsInstance(field, django_models.ForeignKey)
        self.assertEqual(models.Pedido, field.related.parent_model)


class PedidoTestCase(test.TestCase):

    def test_pedido_deve_ter_referencia_para_usuario(self):
        field = models.Pedido._meta.get_field_by_name("usuario")[0]
        self.assertIsInstance(field, django_models.ForeignKey)
        self.assertEqual(auth_models.User, field.related.parent_model)

    def test_pedido_deve_ter_valor(self):
        fields = models.Pedido._meta.get_all_field_names()
        self.assertIn("valor", fields)

    def test_valor_deve_ser_decimalfield(self):
        field = models.Pedido._meta.get_field_by_name("valor")[0]
        self.assertIsInstance(field, django_models.DecimalField)

    def test_valor_deve_ter_10_digitos(self):
        field = models.Pedido._meta.get_field_by_name("valor")[0]
        self.assertEqual(10, field.max_digits)

    def test_valor_deve_ter_duas_casas_decimais(self):
        field = models.Pedido._meta.get_field_by_name("valor")[0]
        self.assertEqual(2, field.decimal_places)

    def test_pedido_deve_ter_metodo_adicionar_item(self):
        produto = vitrine_models.Produto(nome=u"refrigerante genérico", preco=10.0)
        pedido = models.Pedido()
        pedido.adicionar_item(produto)
        pedido.adicionar_item(produto)
        item = pedido._itens[0]
        self.assertIsInstance(item, models.Item)
        self.assertEqual(produto.nome, item.nome)
        self.assertEqual(produto.preco, item.preco)
        self.assertEqual(pedido, item.pedido)
        self.assertEqual(20, pedido.valor)

    def test_pedido_save_deve_salvar_itens(self):
        user = auth_models.User.objects.create(username="utest")
        produto1 = vitrine_models.Produto(nome=u"refri", preco=11)
        produto2 = vitrine_models.Produto(nome=u"refri 2", preco=21)
        produto3 = vitrine_models.Produto(nome=u"refri 3", preco=31)
        pedido = models.Pedido(usuario=user)
        pedido.adicionar_item(produto1)
        pedido.adicionar_item(produto2)
        pedido.adicionar_item(produto3)
        pedido.save()
        self.assertIsNotNone(pedido._itens[0].pk)
        self.assertIsNotNone(pedido._itens[1].pk)
        self.assertIsNotNone(pedido._itens[2].pk)
