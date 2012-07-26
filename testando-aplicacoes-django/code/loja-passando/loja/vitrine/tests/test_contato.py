# -*- coding: utf-8 -*-
import mock
import splinter
from django import forms as django_forms, test
from django.conf import settings
from django.forms import widgets

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
        with mock.patch('loja.vitrine.mailer.EnviadorDeEmail.enviar_email') as enviar_email:
            self.browser.visit("%s/contato" % self.live_server_url)
            self.browser.fill("nome", "Francisco Souza")
            self.browser.fill("email", "fss@corp.globo.com")
            self.browser.fill("mensagem", "Gostei do notebook azul")
            self.browser.find_by_css("button").click()
            enviar_email.assert_called_with(
                assunto=u"Contato pelo site",
                mensagem=u"Gostei do notebook azul",
                remetente=u"fss@corp.globo.com",
                destinatario=settings.EMAIL_ADMIN,
            )


class FormularioContatoTestCase(test.TestCase):

    def test_deve_ter_campo_nome(self):
        self.assertIn("nome", forms.Contato.base_fields)

    def test_nome_deve_ter_no_maximo_255_caracteres(self):
        field = forms.Contato.base_fields["nome"]
        self.assertEqual(255, field.max_length)

    def test_deve_ter_campo_email(self):
        self.assertIn("email", forms.Contato.base_fields)

    def test_campo_email_deve_aceitar_apenas_emails_validos(self):
        field = forms.Contato.base_fields["email"]
        self.assertIsInstance(field, django_forms.EmailField)

    def test_deve_ter_campo_mensagem(self):
        self.assertIn("mensagem", forms.Contato.base_fields)

    def test_mensagem_deve_usar_Textarea_como_widget(self):
        field = forms.Contato.base_fields["mensagem"]
        self.assertIsInstance(field.widget, widgets.Textarea)
