from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Base de dados simulada
ALUNOS = [
    {'matricula': 1, 'nome': 'João', 'idade': 20, 'curso': 'Engenharia', 'email': 'joao@email.com', 'telefone': '(11) 98765-4321', 'periodo': '5º semestre'},
    {'matricula': 2, 'nome': 'Maria', 'idade': 22, 'curso': 'Medicina', 'email': 'maria@email.com', 'telefone': '(11) 98765-4322', 'periodo': '7º semestre'},
    {'matricula': 3, 'nome': 'Pedro', 'idade': 21, 'curso': 'Direito', 'email': 'pedro@email.com', 'telefone': '(11) 98765-4323', 'periodo': '6º semestre'},
    {'matricula': 4, 'nome': 'Ana', 'idade': 19, 'curso': 'Arquitetura', 'email': 'ana@email.com', 'telefone': '(11) 98765-4324', 'periodo': '3º semestre'},
    {'matricula': 5, 'nome': 'Lucas', 'idade': 23, 'curso': 'Administração', 'email': 'lucas@email.com', 'telefone': '(11) 98765-4325', 'periodo': '8º semestre'},
    {'matricula': 6, 'nome': 'Carla', 'idade': 20, 'curso': 'Psicologia', 'email': 'carla@email.com', 'telefone': '(11) 98765-4326', 'periodo': '4º semestre'},
    {'matricula': 7, 'nome': 'Rafael', 'idade': 22, 'curso': 'Ciência da Computação', 'email': 'rafael@email.com', 'telefone': '(11) 98765-4327', 'periodo': '6º semestre'},
    {'matricula': 8, 'nome': 'Fernanda', 'idade': 21, 'curso': 'Engenharia de Software', 'email': 'fernanda@email.com', 'telefone': '(11) 98765-4328', 'periodo': '5º semestre'},
    {'matricula': 9, 'nome': 'Gustavo', 'idade': 19, 'curso': 'Sistemas de Informação', 'email': 'gustavo@email.com', 'telefone': '(11) 98765-4329', 'periodo': '2º semestre'},
    {'matricula': 10, 'nome': 'Beatriz', 'idade': 23, 'curso': 'Análise e Desenvolvimento de Sistemas', 'email': 'beatriz@email.com', 'telefone': '(11) 98765-4330', 'periodo': '7º semestre'},
]

def get_aluno_by_id(id):
    for aluno in ALUNOS:
        if aluno['matricula'] == id:
            return aluno
    return None

# Create your views here.
def alunos_list(request):
    return render(request, 'aluno/alunos_list.html', {'alunos': ALUNOS})

def aluno_detalhe(request, id):
    # Busca o aluno pela matrícula
    aluno = get_aluno_by_id(id)

    if aluno is None:
        raise Http404("Aluno não encontrado")
    
    return render(request, 'aluno/aluno_detail.html', {'aluno': aluno})