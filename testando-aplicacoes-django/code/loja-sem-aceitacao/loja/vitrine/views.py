from django import http
from django.conf import settings
from django.template import response
from django.views.generic import base

from loja.vitrine import forms, mailer


class Contato(base.View):
    template_name = "contato.html"

    def get(self, request):
        return response.TemplateResponse(request, self.template_name, {'form': forms.Contato()})

    def post(self, request):
        f = forms.Contato(request.POST)
        mailer.EnviadorDeEmail().enviar_email(
            assunto=u"Contato pelo site",
            mensagem=f.data["mensagem"],
            remetente=f.data["email"],
            destinatario=settings.EMAIL_ADMIN,
        )
        return http.HttpResponse("Ok")
