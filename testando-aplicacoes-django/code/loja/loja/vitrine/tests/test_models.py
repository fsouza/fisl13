from django import test
from django.db import models as django_models

from loja.vitrine import models


class ProdutoTestCase(test.TestCase):

    def test_produto_deve_ter_nome(self):
        fields = models.Produto._meta.get_all_field_names()
        self.assertIn("nome", fields)

    def test_nome_deve_ser_charfield(self):
        field = models.Produto._meta.get_field_by_name("nome")[0]
        self.assertIsInstance(field, django_models.CharField)

    def test_nome_deve_ter_no_maximo_500_caracteres(self):
        field = models.Produto._meta.get_field_by_name("nome")[0]
        self.assertEqual(500, field.max_length)

    def test_produto_deve_ter_preco(self):
        fields = models.Produto._meta.get_all_field_names()
        self.assertIn("preco", fields)

    def test_preco_deve_ser_decimalfield(self):
        field = models.Produto._meta.get_field_by_name("preco")[0]
        self.assertIsInstance(field, django_models.DecimalField)

    def test_preco_deve_ter_no_maximo_10_digitos(self):
        field = models.Produto._meta.get_field_by_name("preco")[0]
        self.assertEqual(10, field.max_digits)

    def test_preco_deve_ter_duas_casas_decimais(self):
        field = models.Produto._meta.get_field_by_name("preco")[0]
        self.assertEqual(2, field.decimal_places)
