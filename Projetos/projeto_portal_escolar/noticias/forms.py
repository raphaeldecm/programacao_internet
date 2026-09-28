from django import forms

from . import models


class CategoriaForm(forms.Form):
    nome = forms.CharField(
        label="Nome do Formulário",
        max_length=100
    )

class TagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = ["nome"]