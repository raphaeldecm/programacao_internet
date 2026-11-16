from django.shortcuts import render

# Atividade: substituir os exemplos estáticos pelas operações do sistema.


def estudante_lista(request):
    return render(request, "estudante/estudante_lista.html")


def estudante_detalhe(request, pk):
    return render(request, "estudante/estudante_detalhe.html")


def estudante_criar(request):
    return render(request, "estudante/estudante_form.html")


def estudante_editar(request, pk):
    return render(request, "estudante/estudante_form.html")


def estudante_excluir(request, pk):
    return render(request, "estudante/estudante_excluir.html")
