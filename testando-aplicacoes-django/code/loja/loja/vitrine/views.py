from django import http
from django.conf import settings
from django.core import mail
from django.template import response
from django.views.generic import base

from loja.vitrine import forms


class Contato(base.View):
    template_name = "contato.html"

    def get(self, request):
        return response.TemplateResponse(request, self.template_name, {'form': forms.Contato()})

    def post(self, request):
        form = forms.Contato(request.POST)
        mail.send_mail(
            message=form.data["mensagem"],
            from_email=form.data["email"],
            recipient_list=[settings.EMAIL_ADMIN],
            subject=u"Contato pelo site",
        )
        return http.HttpResponse("ok")
