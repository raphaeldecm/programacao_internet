from django.shortcuts import render

# Atividade: substituir os exemplos estáticos pelas operações do sistema.


def curso_lista(request):
    return render(request, "curso/curso_lista.html")


def curso_detalhe(request, pk):
    return render(request, "curso/curso_detalhe.html")


def curso_criar(request):
    return render(request, "curso/curso_form.html")


def curso_editar(request, pk):
    return render(request, "curso/curso_form.html")


def curso_excluir(request, pk):
    return render(request, "curso/curso_excluir.html")
