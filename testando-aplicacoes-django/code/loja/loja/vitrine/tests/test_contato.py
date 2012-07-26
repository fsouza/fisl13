# -*- coding: utf-8 -*-
import splinter
from django import test
from django.conf import settings
from django.core import mail

from loja.vitrine import forms


class PaginaDeContatoTestCase(test.LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = splinter.Browser("firefox")
        super(PaginaDeContatoTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(PaginaDeContatoTestCase, cls).tearDownClass()

    def test_preenche_formulario_e_envia_email(self):
        self.browser.visit("%s/contato" % self.live_server_url)
        self.browser.fill("nome", "Francisco Souza")
        self.browser.fill("email", "fss@corp.globo.com")
        self.browser.fill("mensagem", "Gostei do notebook azul")
        self.browser.find_by_css("button").click()
        email = mail.outbox[0]
        self.assertEqual(u"Contato pelo site", email.subject)
        self.assertEqual(u"Gostei do notebook azul", email.body)
        self.assertEqual(u"fss@corp.globo.com", email.from_email)
        self.assertEqual([settings.EMAIL_ADMIN], email.to)


class FormularioContatoTestCase(test.TestCase):

    def test_deve_ter_campo_nome(self):
        self.assertIn("nome", forms.Contato.base_fields)

    def test_nome_deve_ter_no_maximo_255_caracteres(self):
        field = forms.Contato.base_fields["nome"]
        self.assertEqual(255, field.max_length)
