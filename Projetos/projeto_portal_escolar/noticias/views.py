from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models


# Create your views here.
def categorias_lista_view(request):
    categorias = models.Categoria.objects.all()

    return render(request, "categoria/lista.html", {
        "categorias": categorias
    })

def categoria_detalhe_view(request, categoria_id):
    categoria = models.Categoria.objects.get(id=categoria_id)

    return render(request, "categoria/detalhe.html", {
        "categoria": categoria,
    })

def categoria_create_view(request):
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria criada com sucesso!")
            return redirect("noticias:categorias")
        else:
            messages.error(request, "Erro ao criar categoria. Verifique os dados informados.")
    else:
        form = forms.CategoriaForm()

    return render(request, "categoria/form.html", {
        "form": form,
    })

def categoria_update_view(request, categoria_id):
    categoria = models.Categoria.objects.get(id=categoria_id)

    if request.method == "POST":
        form = forms.CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria atualizada com sucesso!")
            return redirect("noticias:categorias")
        else:
            messages.error(request, "Erro ao atualizar categoria. Verifique os dados informados.")
    else:
        form = forms.CategoriaForm(instance=categoria)

    return render(request, "categoria/form.html", {
        "form": form,
        "categoria": categoria,
    })

def categoria_delete_view(request, categoria_id):
    categoria = models.Categoria.objects.get(id=categoria_id)
    if request.method == "POST":
        try:
            categoria.delete()
            messages.success(request, "Categoria deletada com sucesso!")
            return redirect("noticias:categorias")
        except ProtectedError:
            messages.warning(request, f"{categoria.nome} não pode ser deletada, pois existem notícias associadas a ela.")
            return redirect("noticias:categorias")
    
    return render(request, "categoria/confirmar_exclusao.html", {
            "categoria": categoria,
        })

def tags_lista_view(request):
    tags = models.Tag.objects.all()

    return render(request, "tag/lista.html", {
        "tags": tags
    })

def tag_detalhe_view(request, tag_id):
    tag = models.Tag.objects.get(id=tag_id)

    return render(request, "tag/detalhe.html", {
        "tag": tag,
    })

def tag_create_view(request):
    if request.method == "POST":
        form = forms.TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag criada com sucesso!")
            return redirect("noticias:tags")
        else:
            messages.error(request, "Erro ao criar tag. Verifique os dados informados.")
    else:
        form = forms.TagForm()

    return render(request, "tag/form.html", {
        "form": form,
    })

def tag_update_view(request, tag_id):
    tag = models.Tag.objects.get(id=tag_id)

    if request.method == "POST":
        form = forms.TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag atualizada com sucesso!")
            return redirect("noticias:tags")
        else:
            messages.error(request, "Erro ao atualizar tag. Verifique os dados informados.")
    else:
        form = forms.TagForm(initial={"nome": tag.nome})

    return render(request, "tag/form.html", {
        "form": form,
        "tag": tag,
    })

def tag_delete_view(request, tag_id):
    tag = models.Tag.objects.get(id=tag_id)
    tag.delete()
    return redirect("noticias:tags")

def noticia_create_view(request):
    if request.method == "POST":
        form = forms.NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Notícia criada com sucesso!")
            return redirect("noticias:noticias")
    else:
        form = forms.NoticiaForm()

    return render(request, "noticia/form.html", {
        "form": form,
    })

def noticia_update_view(request, noticia_id):
    noticia = models.Noticia.objects.get(id=noticia_id)

    if request.method == "POST":
        form = forms.NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, "Notícia atualizada com sucesso!")
            return redirect("noticias:noticias")
    else:
        form = forms.NoticiaForm(instance=noticia)

    return render(request, "noticia/form.html", {
        "form": form,
        "noticia": noticia,
    })

def noticia_delete_view(request, noticia_id):
    noticia = models.Noticia.objects.get(id=noticia_id)

    if request.method == "POST":
        noticia.delete()
        messages.success(request, "Notícia deletada com sucesso!")
        return redirect("noticias:noticias")
    
    return render(request, "noticia/confirmar_exclusao.html", {
        "noticia": noticia,
    })

def noticias_lista_view(request):
    noticias = models.Noticia.objects.all()
    categoria = request.GET.get('categoria', '')
    tags_selecionadas = [tag for tag in request.GET.getlist('tag') if tag]

    if request.method == "GET":
        busca = request.GET.get("busca")

        if busca:
            noticias = noticias.filter(titulo__icontains=busca)
        if categoria:
            noticias = noticias.filter(categoria__id=request.GET.get("categoria"))
        if tags_selecionadas:
            noticias = noticias.filter(tags__id__in=tags_selecionadas).distinct()

        coluna = request.GET.get('coluna')
        if coluna:
            if coluna == 'titulo':
                noticias = noticias.order_by('titulo')
            elif coluna == 'data_publicacao':
                noticias = noticias.order_by('data_publicacao')
            elif coluna == 'categoria':
                noticias = noticias.order_by('categoria__nome')

    return render(request, "noticia/lista.html", {
        "noticias": noticias,
        "categorias": models.Categoria.objects.all(),
        "tags": models.Tag.objects.all(),
        "categoria_selecionada": categoria,
        "tags_selecionadas": tags_selecionadas,
    })

def noticia_detalhe_view(request, noticia_id):
    noticia = models.Noticia.objects.get(id=noticia_id)

    return render(request, "noticia/detalhe.html", {
        "noticia": noticia,
    })

