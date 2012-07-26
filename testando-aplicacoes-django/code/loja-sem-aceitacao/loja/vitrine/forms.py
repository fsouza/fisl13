from django import forms
from django.forms import widgets


class Contato(forms.Form):
    nome = forms.CharField(max_length=255)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=widgets.Textarea)
