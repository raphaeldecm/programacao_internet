# Projeto Prático 4 - To-Do List com JavaScript e Django

## 🎯 Objetivo

Criar uma aplicação de lista de tarefas (To-Do List) totalmente funcional utilizando Django no backend e JavaScript no frontend, com interações dinâmicas sem recarregar a página.

---

## 📋 Requisitos do Projeto

### Funcionalidades Principais

1. **Adicionar Tarefa** (AJAX)
   - Formulário para criar nova tarefa
   - Envio sem recarregar página
   - Validação em tempo real

2. **Listar Tarefas**
   - Exibir todas as tarefas
   - Atualizar lista dinamicamente
   - Filtrar por status (todas/pendentes/concluídas)

3. **Marcar como Concluída** (AJAX)
   - Checkbox interativo
   - Atualização instantânea

4. **Editar Tarefa** (AJAX)
   - Edição inline
   - Salvar mudanças sem reload

5. **Deletar Tarefa** (AJAX)
   - Modal de confirmação
   - Remoção instantânea

6. **Busca em Tempo Real**
   - Filtrar tarefas enquanto digita
   - Debounce para otimização

### Requisitos Técnicos

- ✅ Backend: Django (Views + API JSON)
- ✅ Frontend: JavaScript (Fetch API)
- ✅ AJAX para todas as operações CRUD
- ✅ CSRF Protection
- ✅ Validação client-side e server-side
- ✅ Feedback visual (loading, mensagens)
- ✅ Design responsivo

---

## 🗂️ Estrutura do Projeto

```
todo_project/
├── venv/
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tasks/                              # App principal
│   ├── static/
│   │   └── tasks/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── js/
│   │           └── app.js
│   ├── templates/
│   │   └── tasks/
│   │       ├── base.html
│   │       └── index.html
│   ├── views.py
│   └── urls.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 🚀 Passo a Passo

### 1. Setup Inicial

```bash
# Criar projeto
django-admin startproject todo_project .
python manage.py startapp tasks

# Adicionar app no settings.py
INSTALLED_APPS = [
    ...
    'tasks',
]

# Migrar
python manage.py migrate
```

### 2. Configurar URLs

**todo_project/urls.py:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]
```

**tasks/urls.py:**
```python
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    
    # API endpoints
    path('api/tasks/', views.api_tasks, name='api_tasks'),
    path('api/tasks/<int:task_id>/', views.api_task_detail, name='api_task_detail'),
    path('api/tasks/<int:task_id>/toggle/', views.api_task_toggle, name='api_task_toggle'),
]
```

### 3. Criar Views

**tasks/views.py:**
```python
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie

# Simulação de banco de dados (em memória)
# Em produção, use models e banco real
TASKS = [
    {'id': 1, 'titulo': 'Estudar Django', 'concluida': False},
    {'id': 2, 'titulo': 'Fazer exercícios', 'concluida': True},
    {'id': 3, 'titulo': 'Revisar JavaScript', 'concluida': False},
]
NEXT_ID = 4

@ensure_csrf_cookie
def index(request):
    """View principal - renderiza o template"""
    return render(request, 'tasks/index.html')

@require_http_methods(["GET", "POST"])
def api_tasks(request):
    """
    GET: Lista todas as tarefas
    POST: Cria nova tarefa
    """
    global NEXT_ID
    
    if request.method == 'GET':
        # Filtrar por busca
        query = request.GET.get('q', '').lower()
        
        if query:
            tasks_filtered = [
                t for t in TASKS 
                if query in t['titulo'].lower()
            ]
        else:
            tasks_filtered = TASKS
        
        # Filtrar por status
        status = request.GET.get('status', 'all')
        if status == 'pending':
            tasks_filtered = [t for t in tasks_filtered if not t['concluida']]
        elif status == 'completed':
            tasks_filtered = [t for t in tasks_filtered if t['concluida']]
        
        return JsonResponse({
            'success': True,
            'tasks': tasks_filtered
        })
    
    elif request.method == 'POST':
        # Criar nova tarefa
        try:
            data = json.loads(request.body)
            titulo = data.get('titulo', '').strip()
            
            # Validação
            if not titulo:
                return JsonResponse({
                    'success': False,
                    'error': 'Título é obrigatório'
                }, status=400)
            
            if len(titulo) < 3:
                return JsonResponse({
                    'success': False,
                    'error': 'Título deve ter pelo menos 3 caracteres'
                }, status=400)
            
            # Criar tarefa
            nova_tarefa = {
                'id': NEXT_ID,
                'titulo': titulo,
                'concluida': False
            }
            
            TASKS.append(nova_tarefa)
            NEXT_ID += 1
            
            return JsonResponse({
                'success': True,
                'message': 'Tarefa criada com sucesso!',
                'task': nova_tarefa
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'JSON inválido'
            }, status=400)

@require_http_methods(["GET", "PUT", "DELETE"])
def api_task_detail(request, task_id):
    """
    GET: Detalhe da tarefa
    PUT: Atualizar tarefa
    DELETE: Deletar tarefa
    """
    # Buscar tarefa
    task = next((t for t in TASKS if t['id'] == task_id), None)
    
    if not task:
        return JsonResponse({
            'success': False,
            'error': 'Tarefa não encontrada'
        }, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'success': True,
            'task': task
        })
    
    elif request.method == 'PUT':
        # Atualizar tarefa
        try:
            data = json.loads(request.body)
            titulo = data.get('titulo', '').strip()
            
            if not titulo:
                return JsonResponse({
                    'success': False,
                    'error': 'Título é obrigatório'
                }, status=400)
            
            task['titulo'] = titulo
            
            return JsonResponse({
                'success': True,
                'message': 'Tarefa atualizada!',
                'task': task
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'JSON inválido'
            }, status=400)
    
    elif request.method == 'DELETE':
        # Deletar tarefa
        TASKS.remove(task)
        
        return JsonResponse({
            'success': True,
            'message': 'Tarefa deletada com sucesso!'
        })

@require_http_methods(["POST"])
def api_task_toggle(request, task_id):
    """Toggle tarefa concluída/pendente"""
    task = next((t for t in TASKS if t['id'] == task_id), None)
    
    if not task:
        return JsonResponse({
            'success': False,
            'error': 'Tarefa não encontrada'
        }, status=404)
    
    # Toggle
    task['concluida'] = not task['concluida']
    
    return JsonResponse({
        'success': True,
        'task': task
    })
```

### 4. Criar Templates

**tasks/templates/tasks/base.html:**
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}To-Do List{% endblock %}</title>
    
    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- CSS Customizado -->
    <link rel="stylesheet" href="{% static 'tasks/css/style.css' %}">
</head>
<body>
    <nav class="navbar navbar-dark bg-primary">
        <div class="container">
            <span class="navbar-brand mb-0 h1">
                <i class="fas fa-tasks"></i> To-Do List
            </span>
        </div>
    </nav>
    
    <main class="container my-4">
        {% block content %}{% endblock %}
    </main>
    
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- JavaScript -->
    {% block scripts %}{% endblock %}
</body>
</html>
```

**tasks/templates/tasks/index.html:**
```html
{% extends 'tasks/base.html' %}
{% load static %}

{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <div class="card">
            <div class="card-body">
                <h2 class="card-title">Minhas Tarefas</h2>
                
                <!-- Formulário de Nova Tarefa -->
                <form id="form-nova-tarefa" class="mb-4">
                    {% csrf_token %}
                    <div class="input-group">
                        <input 
                            type="text" 
                            id="input-titulo" 
                            class="form-control" 
                            placeholder="Adicionar nova tarefa..."
                            required
                            minlength="3"
                        >
                        <button class="btn btn-primary" type="submit">
                            <i class="fas fa-plus"></i> Adicionar
                        </button>
                    </div>
                    <div id="erro-form" class="text-danger mt-2 small"></div>
                </form>
                
                <!-- Busca e Filtros -->
                <div class="row mb-3">
                    <div class="col-md-6">
                        <input 
                            type="text" 
                            id="input-busca" 
                            class="form-control" 
                            placeholder="Buscar tarefas..."
                        >
                    </div>
                    <div class="col-md-6">
                        <select id="filtro-status" class="form-select">
                            <option value="all">Todas</option>
                            <option value="pending">Pendentes</option>
                            <option value="completed">Concluídas</option>
                        </select>
                    </div>
                </div>
                
                <!-- Loading -->
                <div id="loading" class="text-center my-3" style="display: none;">
                    <div class="spinner-border text-primary" role="status">
                        <span class="visually-hidden">Carregando...</span>
                    </div>
                </div>
                
                <!-- Mensagens -->
                <div id="mensagens"></div>
                
                <!-- Lista de Tarefas -->
                <ul id="lista-tarefas" class="list-group">
                    <!-- Tarefas serão inseridas aqui via JavaScript -->
                </ul>
                
                <!-- Estatísticas -->
                <div class="mt-3 text-muted small">
                    <span>Total: <strong id="total-tarefas">0</strong></span> |
                    <span>Pendentes: <strong id="total-pendentes">0</strong></span> |
                    <span>Concluídas: <strong id="total-concluidas">0</strong></span>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Modal de Confirmação de Deleção -->
<div class="modal fade" id="modalDeletar" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Confirmar Deleção</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                Tem certeza que deseja deletar esta tarefa?
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                <button type="button" class="btn btn-danger" id="btn-confirmar-deletar">Deletar</button>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script src="{% static 'tasks/js/app.js' %}"></script>
{% endblock %}
```

### 5. Criar JavaScript

**tasks/static/tasks/js/app.js:**
```javascript
// Estado da aplicação
let tarefas = [];
let taskIdParaDeletar = null;

// Elementos do DOM
const formNovaTarefa = document.getElementById('form-nova-tarefa');
const inputTitulo = document.getElementById('input-titulo');
const erroForm = document.getElementById('erro-form');
const listaTarefas = document.getElementById('lista-tarefas');
const loading = document.getElementById('loading');
const mensagens = document.getElementById('mensagens');
const inputBusca = document.getElementById('input-busca');
const filtroStatus = document.getElementById('filtro-status');
const totalTarefas = document.getElementById('total-tarefas');
const totalPendentes = document.getElementById('total-pendentes');
const totalConcluidas = document.getElementById('total-concluidas');
const modalDeletar = new bootstrap.Modal(document.getElementById('modalDeletar'));
const btnConfirmarDeletar = document.getElementById('btn-confirmar-deletar');

// CSRF Token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// Carregar tarefas
async function carregarTarefas() {
    mostrarLoading(true);
    
    try {
        const query = inputBusca.value;
        const status = filtroStatus.value;
        
        const url = `/api/tasks/?q=${query}&status=${status}`;
        const response = await fetch(url);
        const data = await response.json();
        
        if (data.success) {
            tarefas = data.tasks;
            renderizarTarefas();
            atualizarEstatisticas();
        }
    } catch (error) {
        mostrarMensagem('Erro ao carregar tarefas', 'danger');
    } finally {
        mostrarLoading(false);
    }
}

// Renderizar tarefas
function renderizarTarefas() {
    if (tarefas.length === 0) {
        listaTarefas.innerHTML = `
            <li class="list-group-item text-center text-muted">
                <i class="fas fa-inbox fa-3x mb-3"></i>
                <p>Nenhuma tarefa encontrada</p>
            </li>
        `;
        return;
    }
    
    listaTarefas.innerHTML = tarefas.map(task => `
        <li class="list-group-item" data-task-id="${task.id}">
            <div class="d-flex align-items-center">
                <input 
                    type="checkbox" 
                    class="form-check-input me-3 checkbox-tarefa" 
                    ${task.concluida ? 'checked' : ''}
                    data-task-id="${task.id}"
                >
                
                <span 
                    class="flex-grow-1 titulo-tarefa ${task.concluida ? 'text-decoration-line-through text-muted' : ''}"
                    data-task-id="${task.id}"
                >
                    ${task.titulo}
                </span>
                
                <button 
                    class="btn btn-sm btn-outline-primary me-2 btn-editar"
                    data-task-id="${task.id}"
                >
                    <i class="fas fa-edit"></i>
                </button>
                
                <button 
                    class="btn btn-sm btn-outline-danger btn-deletar"
                    data-task-id="${task.id}"
                >
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        </li>
    `).join('');
    
    // Adicionar event listeners
    adicionarEventListeners();
}

// Adicionar event listeners nas tarefas
function adicionarEventListeners() {
    // Checkboxes
    document.querySelectorAll('.checkbox-tarefa').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            toggleTarefa(parseInt(this.dataset.taskId));
        });
    });
    
    // Botões deletar
    document.querySelectorAll('.btn-deletar').forEach(btn => {
        btn.addEventListener('click', function() {
            taskIdParaDeletar = parseInt(this.dataset.taskId);
            modalDeletar.show();
        });
    });
    
    // Botões editar
    document.querySelectorAll('.btn-editar').forEach(btn => {
        btn.addEventListener('click', function() {
            editarTarefa(parseInt(this.dataset.taskId));
        });
    });
}

// Criar nova tarefa
formNovaTarefa.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const titulo = inputTitulo.value.trim();
    erroForm.textContent = '';
    
    if (titulo.length < 3) {
        erroForm.textContent = 'Título deve ter pelo menos 3 caracteres';
        return;
    }
    
    try {
        const response = await fetch('/api/tasks/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ titulo })
        });
        
        const data = await response.json();
        
        if (data.success) {
            inputTitulo.value = '';
            mostrarMensagem(data.message, 'success');
            await carregarTarefas();
        } else {
            erroForm.textContent = data.error;
        }
    } catch (error) {
        mostrarMensagem('Erro ao criar tarefa', 'danger');
    }
});

// Toggle tarefa
async function toggleTarefa(taskId) {
    try {
        const response = await fetch(`/api/tasks/${taskId}/toggle/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            }
        });
        
        const data = await response.json();
        
        if (data.success) {
            await carregarTarefas();
        }
    } catch (error) {
        mostrarMensagem('Erro ao atualizar tarefa', 'danger');
    }
}

// Deletar tarefa
btnConfirmarDeletar.addEventListener('click', async function() {
    if (!taskIdParaDeletar) return;
    
    try {
        const response = await fetch(`/api/tasks/${taskIdParaDeletar}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrftoken
            }
        });
        
        const data = await response.json();
        
        if (data.success) {
            mostrarMensagem(data.message, 'success');
            await carregarTarefas();
            modalDeletar.hide();
        }
    } catch (error) {
        mostrarMensagem('Erro ao deletar tarefa', 'danger');
    }
});

// Editar tarefa (inline)
async function editarTarefa(taskId) {
    const task = tarefas.find(t => t.id === taskId);
    if (!task) return;
    
    const novoTitulo = prompt('Editar tarefa:', task.titulo);
    
    if (novoTitulo === null || novoTitulo.trim() === '') return;
    
    try {
        const response = await fetch(`/api/tasks/${taskId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ titulo: novoTitulo })
        });
        
        const data = await response.json();
        
        if (data.success) {
            mostrarMensagem(data.message, 'success');
            await carregarTarefas();
        } else {
            alert(data.error);
        }
    } catch (error) {
        mostrarMensagem('Erro ao editar tarefa', 'danger');
    }
}

// Busca em tempo real (com debounce)
let debounceTimer;
inputBusca.addEventListener('input', function() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
        carregarTarefas();
    }, 300);
});

// Filtro de status
filtroStatus.addEventListener('change', function() {
    carregarTarefas();
});

// Atualizar estatísticas
function atualizarEstatisticas() {
    totalTarefas.textContent = tarefas.length;
    totalPendentes.textContent = tarefas.filter(t => !t.concluida).length;
    totalConcluidas.textContent = tarefas.filter(t => t.concluida).length;
}

// Mostrar loading
function mostrarLoading(show) {
    loading.style.display = show ? 'block' : 'none';
}

// Mostrar mensagem
function mostrarMensagem(texto, tipo) {
    mensagens.innerHTML = `
        <div class="alert alert-${tipo} alert-dismissible fade show" role="alert">
            ${texto}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    
    // Auto-remover após 3 segundos
    setTimeout(() => {
        mensagens.innerHTML = '';
    }, 3000);
}

// Carregar tarefas ao iniciar
document.addEventListener('DOMContentLoaded', function() {
    carregarTarefas();
});
```

### 6. CSS

**tasks/static/tasks/css/style.css:**
```css
body {
    background-color: #f5f5f5;
    min-height: 100vh;
}

.list-group-item {
    transition: all 0.3s ease;
}

.list-group-item:hover {
    background-color: #f8f9fa;
}

.titulo-tarefa {
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn {
    transition: all 0.3s ease;
}

.checkbox-tarefa {
    cursor: pointer;
    width: 20px;
    height: 20px;
}

/* Animação para novas tarefas */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.list-group-item {
    animation: slideIn 0.3s ease;
}
```

---

## ✅ Checklist de Entrega

- [ ] Adicionar tarefas funcionando
- [ ] Listar tarefas
- [ ] Marcar como concluída
- [ ] Editar tarefa
- [ ] Deletar tarefa com confirmação
- [ ] Busca em tempo real
- [ ] Filtro por status
- [ ] Estatísticas atualizadas
- [ ] CSRF protection
- [ ] Validação
- [ ] Feedback visual (loading, mensagens)
- [ ] Design responsivo
- [ ] Código organizado e comentado

---

## 🎨 Extras (Opcional)

- [ ] Drag and drop para reordenar
- [ ] Categorias de tarefas
- [ ] Prioridade (alta, média, baixa)
- [ ] Data de vencimento
- [ ] Notificações
- [ ] Modo escuro
- [ ] LocalStorage (backup local)
- [ ] Animações mais elaboradas

---

## 📊 Critérios de Avaliação

| Critério | Pontos |
|----------|--------|
| CRUD completo funcionando | 3.0 |
| AJAX em todas as operações | 2.0 |
| Busca e filtros | 1.5 |
| CSRF e validação | 1.0 |
| Interface e usabilidade | 1.5 |
| Código organizado | 1.0 |
| **Total** | **10.0** |

---

## 🚀 Como Executar

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate

# Instalar Django
pip install django

# Migrar
python manage.py migrate

# Rodar servidor
python manage.py runserver

# Acessar
http://127.0.0.1:8000/
```

---

Boa sorte! 🎉
