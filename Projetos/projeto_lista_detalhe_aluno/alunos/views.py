from django.shortcuts import render

from . import models


# Create your views here.
def alunos_list(request):
    alunos = models.Aluno.objects.all()
    return render(request, 'aluno/alunos_list.html', {'alunos': alunos})

def aluno_detalhe(request, id):
    # Busca o aluno pela matrícula
    try:
        aluno = models.Aluno.objects.get(id=id)
    except models.Aluno.DoesNotExist:
        aluno = None
    return render(request, 'aluno/aluno_detail.html', {'aluno': aluno})