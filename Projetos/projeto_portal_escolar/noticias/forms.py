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

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = models.Noticia
        fields = ["titulo", "texto", "categoria", "tags"]

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "texto": forms.Textarea(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"}),
        }