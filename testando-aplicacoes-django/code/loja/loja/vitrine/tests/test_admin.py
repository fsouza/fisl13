# -*- coding: utf-8 -*-
from django import test
from django.contrib import admin as django_admin

from loja.vitrine import admin, models


class ProdutoAdminTestCase(test.TestCase):

    def test_produto_deve_estar_registrado(self):
        self.assertIn(models.Produto, django_admin.site._registry)
