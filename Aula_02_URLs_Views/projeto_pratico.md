# Projeto Prático 2 - Site Multi-Páginas

## 🎯 Objetivo

Criar um site institucional multi-páginas usando Django, aplicando os conceitos de **apps**, URLs, roteamento, views, templates e arquivos estáticos.

> **Novidade desta unidade:** Você criará seu **primeiro app Django**! Apps são componentes reutilizáveis que organizam funcionalidades específicas do seu projeto.

---

## 🧩 O que são Apps Django?

No Django, um **projeto** é uma coleção de configurações e **apps**. Um **app** é um módulo web que faz algo específico (blog, loja, fórum, etc.).

**Diferenças:**
- **Projeto:** configuração geral (settings, URLs principais)
- **App:** funcionalidade específica com seus próprios models, views, templates

**Vantagens:**
- ✅ Organização modular
- ✅ Reutilização em outros projetos
- ✅ Separação de responsabilidades
- ✅ Manutenção facilitada

---

## 📋 Requisitos do Projeto

### Funcionalidades

1. **Página Inicial** (`/`)
   - Apresentação da empresa/projeto
   - Links para outras páginas
   - Banner de destaque

2. **Página Sobre** (`/sobre/`)
   - Informações sobre a empresa/projeto
   - Missão, visão e valores
   - História

3. **Página de Serviços** (`/servicos/`)
   - Lista de serviços oferecidos
   - Descrição de cada serviço

4. **Página de Contato** (`/contato/`)
   - Formulário de contato
   - Informações de contato (email, telefone)
   - Mapa (pode ser iframe do Google Maps)

5. **Página de Equipe** (`/equipe/`)
   - Lista de membros da equipe
   - Foto, nome e cargo de cada membro

### Requisitos Técnicos

- ✅ Usar ambiente virtual
- ✅ Django 5.x
- ✅ Templates com herança (base.html)
- ✅ Arquivos estáticos (CSS, JS, imagens)
- ✅ URLs nomeadas
- ✅ Navegação funcional entre páginas
- ✅ Design responsivo (pode usar Bootstrap)
- ✅ Código organizado e comentado

---

## 🗂️ Estrutura do Projeto

```
site_institucional/
├── venv/
├── site_institucional/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── institucional/              # App principal
│   ├── static/
│   │   └── institucional/
│   │       ├── css/
│   │       │   └── style.css
│   │       ├── js/
│   │       │   └── script.js
│   │       └── img/
│   │           └── logo.png
│   ├── templates/
│   │   └── institucional/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── sobre.html
│   │       ├── servicos.html
│   │       ├── contato.html
│   │       └── equipe.html
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Passo a Passo

### 1. Setup Inicial

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar Django
pip install django

# Criar projeto
django-admin startproject site_institucional .
```

---

### 2. Criar seu Primeiro App

#### 2.1. Comando para criar app

```bash
python manage.py startapp institucional
```

Este comando cria a seguinte estrutura:

```
institucional/
├── __init__.py          # Torna o diretório um pacote Python
├── admin.py            # Configurações do Django Admin
├── apps.py             # Configurações do app
├── migrations/         # Histórico de mudanças no banco
│   └── __init__.py
├── models.py           # Modelos (estrutura de dados)
├── tests.py            # Testes automatizados
└── views.py            # Lógica de visualização
```

#### 2.2. Registrar o app no projeto

Abra `site_institucional/settings.py` e adicione o app:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'institucional',  # ⬅️ Seu app
]
```

> **Por que registrar?** O Django precisa saber quais apps fazem parte do projeto para carregar seus templates, static files, migrations, etc.

---

### 3. Configurar URLs

**site_institucional/urls.py:**
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('institucional.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

**institucional/urls.py:**
```python
from django.urls import path
from . import views

app_name = 'institucional'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('servicos/', views.servicos, name='servicos'),
    path('contato/', views.contato, name='contato'),
    path('equipe/', views.equipe, name='equipe'),
]
```

---

### 4. Criar Views

**institucional/views.py:**
```python
from django.shortcuts import render

def index(request):
    context = {
        'titulo': 'Página Inicial',
        'descricao': 'Bem-vindo ao nosso site!',
    }
    return render(request, 'institucional/index.html', context)

def sobre(request):
    context = {
        'titulo': 'Sobre Nós',
        'missao': 'Nossa missão é...',
        'visao': 'Nossa visão é...',
        'valores': ['Integridade', 'Qualidade', 'Inovação'],
    }
    return render(request, 'institucional/sobre.html', context)

def servicos(request):
    servicos_lista = [
        {
            'titulo': 'Desenvolvimento Web',
            'descricao': 'Criamos sites modernos e responsivos',
            'icone': 'fa-code'
        },
        {
            'titulo': 'Consultoria',
            'descricao': 'Consultoría especializada em tecnologia',
            'icone': 'fa-lightbulb'
        },
        {
            'titulo': 'Suporte',
            'descricao': 'Suporte técnico 24/7',
            'icone': 'fa-headset'
        },
    ]
    context = {
        'titulo': 'Nossos Serviços',
        'servicos': servicos_lista,
    }
    return render(request, 'institucional/servicos.html', context)

def contato(request):
    context = {
        'titulo': 'Fale Conosco',
        'email': 'contato@empresa.com',
        'telefone': '(11) 1234-5678',
        'endereco': 'Rua Exemplo, 123 - São Paulo',
    }
    return render(request, 'institucional/contato.html', context)

def equipe(request):
    membros = [
        {
            'nome': 'João Silva',
            'cargo': 'CEO',
            'foto': 'img/joao.jpg',
        },
        {
            'nome': 'Maria Santos',
            'cargo': 'CTO',
            'foto': 'img/maria.jpg',
        },
        {
            'nome': 'Pedro Costa',
            'cargo': 'Desenvolvedor',
            'foto': 'img/pedro.jpg',
        },
    ]
    context = {
        'titulo': 'Nossa Equipe',
        'membros': membros,
    }
    return render(request, 'institucional/equipe.html', context)
```

---

### 5. Criar Template Base

**institucional/templates/institucional/base.html:**
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Meu Site{% endblock %}</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- CSS Customizado -->
    <link rel="stylesheet" href="{% static 'institucional/css/style.css' %}">
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{% url 'institucional:index' %}">
                <img src="{% static 'institucional/img/logo.png' %}" alt="Logo" height="30">
                Minha Empresa
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'institucional:index' %}">Início</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'institucional:sobre' %}">Sobre</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'institucional:servicos' %}">Serviços</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'institucional:equipe' %}">Equipe</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'institucional:contato' %}">Contato</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Conteúdo -->
    <main>
        {% block content %}{% endblock %}
    </main>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-4 mt-5">
        <div class="container">
            <p>&copy; 2026 Minha Empresa. Todos os direitos reservados.</p>
            <div class="social-links">
                <a href="#" class="text-white me-3"><i class="fab fa-facebook"></i></a>
                <a href="#" class="text-white me-3"><i class="fab fa-twitter"></i></a>
                <a href="#" class="text-white me-3"><i class="fab fa-instagram"></i></a>
                <a href="#" class="text-white"><i class="fab fa-linkedin"></i></a>
            </div>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- JS Customizado -->
    <script src="{% static 'institucional/js/script.js' %}"></script>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

### 6. Criar Templates de Páginas

**institucional/templates/institucional/index.html:**
```html
{% extends 'institucional/base.html' %}
{% load static %}

{% block title %}{{ titulo }} - Minha Empresa{% endblock %}

{% blockcontent %}
<div class="hero bg-primary text-white text-center py-5">
    <div class="container">
        <h1 class="display-4">Bem-vindo à Minha Empresa</h1>
        <p class="lead">{{ descricao }}</p>
        <a href="{% url 'institucional:contato' %}" class="btn btn-light btn-lg">Entre em Contato</a>
    </div>
</div>

<div class="container my-5">
    <div class="row">
        <div class="col-md-4 text-center mb-4">
            <i class="fas fa-rocket fa-3x text-primary mb-3"></i>
            <h3>Inovação</h3>
            <p>Soluções modernas e inovadoras</p>
        </div>
        <div class="col-md-4 text-center mb-4">
            <i class="fas fa-users fa-3x text-primary mb-3"></i>
            <h3>Equipe Qualificada</h3>
            <p>Profissionais experientes</p>
        </div>
        <div class="col-md-4 text-center mb-4">
            <i class="fas fa-star fa-3x text-primary mb-3"></i>
            <h3>Qualidade</h3>
            <p>Comprometimento com a excelência</p>
        </div>
    </div>
</div>
{% endblock %}
```

---

## ✅ Checklist de Entrega

Verifique se seu projeto tem:

- [ ] Ambiente virtual configurado
- [ ] Django instalado e funcionando
- [ ] App criado e registrado
- [ ] 5 páginas funcionais
- [ ] Template base com herança
- [ ] Navegação entre páginas
- [ ] Arquivos estáticos (CSS/JS)
- [ ] URLs nomeadas
- [ ] Design responsivo
- [ ] requirements.txt
- [ ] README.md com instruções
- [ ] .gitignore configurado
- [ ] Código comentado

---

## 🎨 Extras (Opcional)

- [ ] Formulário de contato funcional (enviando dados por POST)
- [ ] Página404 personalizada
- [ ] Animações CSS
- [ ] Dark mode toggle
- [ ] Galeria de imagens
- [ ] Depoimentos de clientes
- [ ] FAQ (Perguntas Frequentes)

---

## 📊 Critérios de Avaliação

| Critério | Pontos |
|----------|--------|
| Funcionalidade (todas as páginas funcionam) | 3.0 |
| URLs e roteamento corretos | 2.0 |
| Templates com herança | 2.0 |
| Arquivos estáticos configurados | 1.0 |
| Design e usabilidade | 1.5 |
| Código organizado e comentado | 0.5 |
| **Total** | **10.0** |

---

## 🚀 Como Executar

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor
python manage.py runserver

# Acessar no navegador
http://127.0.0.1:8000/
```

---

Boa sorte! 🎉
