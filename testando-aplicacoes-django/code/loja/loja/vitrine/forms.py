from django import forms


class Contato(forms.Form):
    nome = forms.CharField(max_length=255)
