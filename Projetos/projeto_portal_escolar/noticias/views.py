from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models

# Create your views here.
def categorias_lista_view(request):
    categorias = models.Categoria.objects.all()

    print("List Method:", request.method)

    return render(request, "categoria/lista.html", {
        "categorias": categorias
    })

def categoria_detalhe_view(request, categoria_id):
    categoria = models.Categoria.objects.get(id=categoria_id)

    print("Detail Method:", request.method)

    return render(request, "categoria/detalhe.html", {
        "categoria": categoria,
    })

def categoria_create_view(request):
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            models.Categoria.objects.create(
                nome=nome
            )
            return redirect("noticias:categorias")
    else:
        form = forms.CategoriaForm()

    return render(request, "categoria/form.html", {
        "form": form,
    })

def categoria_update_view(request, categoria_id):
    categoria = models.Categoria.objects.get(id=categoria_id)

    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            categoria.nome = form.cleaned_data["nome"]
            categoria.save()
            return redirect("noticias:categorias")
    else:
        form = forms.CategoriaForm(initial={"nome": categoria.nome})

    return render(request, "categoria/form.html", {
        "form": form,
        "categoria": categoria,
    })

def categoria_delete_view(request, categoria_id):
    categoria = models.Categoria.objects.get(id=categoria_id)
    categoria.delete()
    return redirect("noticias:categorias")

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
            return redirect("noticias:tags")
    else:
        form = forms.TagForm()

    return render(request, "tag/form.html", {
        "form": form,
    })

def tag_update_view(request, tag_id):
    tag = models.Tag.objects.get(id=tag_id)

    if request.method == "POST":
        form = forms.TagForm(request.POST)
        if form.is_valid():
            tag.nome = form.cleaned_data["nome"]
            tag.save()
            return redirect("noticias:tags")
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
            return redirect("noticias:noticias")
    else:
        form = forms.NoticiaForm()

    return render(request, "noticia/form.html", {
        "form": form,
    })

def noticia_update_view(request, noticia_id):
    noticia = models.Noticia.objects.get(id=noticia_id)

    if request.method == "POST":
        form = forms.NoticiaForm(request.POST)
        if form.is_valid():
            noticia.titulo = form.cleaned_data["titulo"]
            noticia.texto = form.cleaned_data["texto"]
            noticia.categoria = form.cleaned_data["categoria"]
            noticia.tags.set(form.cleaned_data["tags"])
            noticia.save()
            return redirect("noticias:noticias")
    else:
        form = forms.NoticiaForm(initial={
            "titulo": noticia.titulo,
            "texto": noticia.texto,
            "categoria": noticia.categoria,
            "tags": noticia.tags.all(),
        })

    return render(request, "noticia/form.html", {
        "form": form,
        "noticia": noticia,
    })

def noticia_delete_view(request, noticia_id):
    noticia = models.Noticia.objects.get(id=noticia_id)
    noticia.delete()
    return redirect("noticias:noticias")

def noticias_lista_view(request):
    noticias = models.Noticia.objects.all()

    return render(request, "noticia/lista.html", {
        "noticias": noticias
    })

def noticia_detalhe_view(request, noticia_id):
    noticia = models.Noticia.objects.get(id=noticia_id)

    return render(request, "noticia/detalhe.html", {
        "noticia": noticia,
    })

