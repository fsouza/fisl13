from django import test
from django.core import urlresolvers
from django.template import response

from loja.vitrine import forms, views


class ContatoViewTestCase(test.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.factory = test.RequestFactory()

    def test_deve_responder_pela_url_contato(self):
        r = urlresolvers.resolve("/contato")
        expected_func = views.Contato.as_view()
        got_func = r.func
        self.assertEqual(expected_func.func_name, got_func.func_name)

    def test_deve_renderizar_template_contato_html(self):
        self.assertEqual("contato.html", views.Contato.template_name)

    def test_get_deve_retornar_template_response(self):
        request = self.factory.get("/contato")
        v = views.Contato()
        resp = v.get(request)
        self.assertIsInstance(resp, response.TemplateResponse)
        self.assertEqual(v.template_name, resp.template_name)

    def test_get_deve_incluir_instancia_do_formulario_de_contato_no_contexto(self):
        request = self.factory.get("/contato")
        v = views.Contato()
        resp = v.get(request)
        self.assertIsInstance(resp.context_data["form"], forms.Contato)
