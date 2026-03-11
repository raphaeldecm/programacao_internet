# Projeto Prático 3 - Blog com Templates

## 🎯 Objetivo

Criar um blog funcional utilizando Django Template Language, aplicando herança de templates, tags, filtros e arquivos estáticos.

---

## 📋 Requisitos do Projeto

### Funcionalidades Principais

1. **Página Inicial** (`/`)
   - Banner de destaque
   - Cards com os 6 posts mais recentes
   - Sidebar com categorias

2. **Lista de Posts** (`/blog/`)
   - Lista completa de posts
   - Filtro por categoria
   - Busca por título

3. **Detalhe do Post** (`/blog/<int:id>/`)
   - Título, data, autor
   - Conteúdo completo
   - Posts relacionados

4. **Posts por Categoria** (`/blog/categoria/<slug>/`)
   - Lista de posts da categoria
   - Informações da categoria

5. **Sobre** (`/sobre/`)
   - Informações sobre o blog
   - Equipe

### Requisitos Técnicos

- ✅ Template base com herança
- ✅ Navbar e footer em partials
- ✅ Uso correto de tags ({% for %}, {% if %}, {% url %})
- ✅ Uso de filtros (date, truncatewords, etc)
- ✅ Arquivos estáticos (CSS, JS, imagens)
- ✅ Design responsivo (Bootstrap ou CSS próprio)
- ✅ Namespaces em URLs
- ✅ CSRF protection em formulários

---

## 🗂️ Estrutura do Projeto

```
blog_projeto/
├── venv/
├── blog_projeto/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── blog/                               # App principal
│   ├── static/
│   │   └── blog/
│   │       ├── css/
│   │       │   └── style.css
│   │       ├── js/
│   │       │   └── script.js
│   │       └── img/
│   │           └── default-post.jpg
│   ├── templates/
│   │   ├── base.html
│   │   ├── partials/
│   │   │   ├── navbar.html
│   │   │   ├── footer.html
│   │   │   └── post_card.html
│   │   └── blog/
│   │       ├── home.html
│   │       ├── lista.html
│   │       ├── detalhe.html
│   │       ├── categoria.html
│   │       └── sobre.html
│   ├── views.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

---

## 🚀 Passo a Passo

### 1. Setup Inicial

```bash
# Criar projeto
django-admin startproject blog_projeto .
python manage.py startapp blog

# Adicionar app no settings.py
INSTALLED_APPS = [
    ...
    'blog',
]
```

### 2. Configurar URLs

**blog_projeto/urls.py:**
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**blog/urls.py:**
```python
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.lista_posts, name='lista'),
    path('blog/<int:post_id>/', views.detalhe_post, name='detalhe'),
    path('blog/categoria/<slug:slug>/', views.posts_categoria, name='categoria'),
    path('sobre/', views.sobre, name='sobre'),
    path('buscar/', views.buscar, name='buscar'),
]
```

### 3. Criar Views com Dados Simulados

**blog/views.py:**
```python
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta

# Dados simulados (em uma aplicação real, viriam do banco)
CATEGORIAS = [
    {'id': 1, 'nome': 'Tecnologia', 'slug': 'tecnologia'},
    {'id': 2, 'nome': 'Ciência', 'slug': 'ciencia'},
    {'id': 3, 'nome': 'Programação', 'slug': 'programacao'},
]

POSTS = [
    {
        'id': 1,
        'titulo': 'Introdução ao Django',
        'slug': 'introducao-django',
        'resumo': 'Aprenda os conceitos básicos do Django.',
        'conteudo': 'Django é um framework web Python de alto nível que permite desenvolvimento rápido...',
        'autor': 'João Silva',
        'data': datetime.now() - timedelta(days=2),
        'categoria_id': 3,
        'categoria': 'Programação',
        'imagem': 'blog/img/django.jpg',
        'visualizacoes': 150,
    },
    {
        'id': 2,
        'titulo': 'Python para Iniciantes',
        'slug': 'python-iniciantes',
        'resumo': 'Guia completo para começar com Python.',
        'conteudo': 'Python é uma linguagem de programação de alto nível...',
        'autor': 'Maria Santos',
        'data': datetime.now() - timedelta(days=5),
        'categoria_id': 3,
        'categoria': 'Programação',
        'imagem': 'blog/img/python.jpg',
        'visualizacoes': 230,
    },
    {
        'id': 3,
        'titulo': 'Inteligência Artificial em 2026',
        'slug': 'ia-2026',
        'resumo': 'As últimas tendências em IA.',
        'conteudo': 'A inteligência artificial está revolucionando...',
        'autor': 'Pedro Costa',
        'data': datetime.now() - timedelta(days=1),
        'categoria_id': 1,
        'categoria': 'Tecnologia',
        'imagem': 'blog/img/ia.jpg',
        'visualizacoes': 450,
    },
    # Adicione mais posts...
]

def home(request):
    # Posts mais recentes
    posts_recentes = sorted(POSTS, key=lambda x: x['data'], reverse=True)[:6]
    
    context = {
        'posts': posts_recentes,
        'categorias': CATEGORIAS,
    }
    return render(request, 'blog/home.html', context)

def lista_posts(request):
    # Filtrar por categoria se fornecido
    categoria_slug = request.GET.get('categoria')
    posts = POSTS
    
    if categoria_slug:
        posts = [p for p in POSTS if p['categoria'].lower() == categoria_slug]
    
    context = {
        'posts': posts,
        'categorias': CATEGORIAS,
    }
    return render(request, 'blog/lista.html', context)

def detalhe_post(request, post_id):
    # Buscar post por ID
    post = next((p for p in POSTS if p['id'] == post_id), None)
    
    if not post:
        from django.http import Http404
        raise Http404("Post não encontrado")
    
    # Posts relacionados (mesma categoria)
    posts_relacionados = [
        p for p in POSTS 
        if p['categoria_id'] == post['categoria_id'] and p['id'] != post['id']
    ][:3]
    
    context = {
        'post': post,
        'posts_relacionados': posts_relacionados,
    }
    return render(request, 'blog/detalhe.html', context)

def posts_categoria(request, slug):
    # Buscar categoria
    categoria = next((c for c in CATEGORIAS if c['slug'] == slug), None)
    
    if not categoria:
        from django.http import Http404
        raise Http404("Categoria não encontrada")
    
    # Filtrar posts da categoria
    posts = [p for p in POSTS if p['categoria_id'] == categoria['id']]
    
    context = {
        'categoria': categoria,
        'posts': posts,
    }
    return render(request, 'blog/categoria.html', context)

def sobre(request):
    equipe = [
        {'nome': 'João Silva', 'cargo': 'Editor Chefe', 'bio': 'Jornalista com 10 anos de experiência'},
        {'nome': 'Maria Santos', 'cargo': 'Redatora', 'bio': 'Especialista em tecnologia'},
        {'nome': 'Pedro Costa', 'cargo': 'Desenvolvedor', 'bio': 'Full-stack developer'},
    ]
    
    context = {
        'equipe': equipe,
    }
    return render(request, 'blog/sobre.html', context)

def buscar(request):
    query = request.GET.get('q', '')
    
    if query:
        posts = [
            p for p in POSTS 
            if query.lower() in p['titulo'].lower() or query.lower() in p['resumo'].lower()
        ]
    else:
        posts = []
    
    context = {
        'posts': posts,
        'query': query,
    }
    return render(request, 'blog/lista.html', context)
```

### 4. Criar Template Base

**blog/templates/base.html:**
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Meu Blog{% endblock %}</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- CSS Customizado -->
    <link rel="stylesheet" href="{% static 'blog/css/style.css' %}">
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% include 'partials/navbar.html' %}
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    {% include 'partials/footer.html' %}
    
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- JS Customizado -->
    <script src="{% static 'blog/js/script.js' %}"></script>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### 5. Criar Partials

**blog/templates/partials/navbar.html:**
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="{% url 'blog:home' %}">
            <i class="fas fa-blog"></i> Meu Blog
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'blog:home' %}">Início</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'blog:lista' %}">Posts</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="categoriasDropdown" role="button" data-bs-toggle="dropdown">
                        Categorias
                    </a>
                    <ul class="dropdown-menu">
                        {% for categoria in categorias %}
                        <li>
                            <a class="dropdown-item" href="{% url 'blog:categoria' slug=categoria.slug %}">
                                {{ categoria.nome }}
                            </a>
                        </li>
                        {% endfor %}
                    </ul>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'blog:sobre' %}">Sobre</a>
                </li>
            </ul>
            
            <!-- Busca -->
            <form class="d-flex ms-3" action="{% url 'blog:buscar' %}" method="get">
                <input class="form-control me-2" type="search" name="q" placeholder="Buscar...">
                <button class="btn btn-outline-light" type="submit">
                    <i class="fas fa-search"></i>
                </button>
            </form>
        </div>
    </div>
</nav>
```

**blog/templates/partials/footer.html:**
```html
<footer class="bg-dark text-white text-center py-4 mt-5">
    <div class="container">
        <p class="mb-2">&copy; 2026 Meu Blog. Todos os direitos reservados.</p>
        <div class="social-links">
            <a href="#" class="text-white me-3"><i class="fab fa-facebook fa-2x"></i></a>
            <a href="#" class="text-white me-3"><i class="fab fa-twitter fa-2x"></i></a>
            <a href="#" class="text-white me-3"><i class="fab fa-instagram fa-2x"></i></a>
            <a href="#" class="text-white"><i class="fab fa-linkedin fa-2x"></i></a>
        </div>
    </div>
</footer>
```

**blog/templates/partials/post_card.html:**
```html
<div class="card h-100 shadow-sm">
    <div class="card-body">
        <span class="badge bg-primary mb-2">{{ post.categoria }}</span>
        <h5 class="card-title">{{ post.titulo }}</h5>
        <p class="card-text text-muted small">
            <i class="far fa-calendar"></i> {{ post.data|date:"d/m/Y" }}
            <i class="far fa-user ms-2"></i> {{ post.autor }}
            <i class="far fa-eye ms-2"></i> {{ post.visualizacoes }}
        </p>
        <p class="card-text">{{ post.resumo|truncatewords:20 }}</p>
        <a href="{% url 'blog:detalhe' post_id=post.id %}" class="btn btn-primary">
            Ler mais <i class="fas fa-arrow-right"></i>
        </a>
    </div>
</div>
```

### 6. Criar Páginas

**blog/templates/blog/home.html:**
```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Início - {{ block.super }}{% endblock %}

{% block content %}
<!-- Hero Section -->
<div class="hero bg-primary text-white text-center py-5">
    <div class="container">
        <h1 class="display-4">Bem-vindo ao Meu Blog</h1>
        <p class="lead">Artigos sobre tecnologia, programação e muito mais</p>
    </div>
</div>

<!-- Posts Recentes -->
<section class="container my-5">
    <h2 class="mb-4">Posts Recentes</h2>
    <div class="row">
        {% for post in posts %}
        <div class="col-md-4 mb-4">
            {% include 'partials/post_card.html' %}
        </div>
        {% empty %}
        <div class="col-12">
            <p class="text-center">Nenhum post disponível.</p>
        </div>
        {% endfor %}
    </div>
    
    <div class="text-center mt-4">
        <a href="{% url 'blog:lista' %}" class="btn btn-primary btn-lg">
            Ver Todos os Posts
        </a>
    </div>
</section>

<!-- Categorias -->
<section class="bg-light py-5">
    <div class="container">
        <h2 class="mb-4 text-center">Categorias</h2>
        <div class="row">
            {% for categoria in categorias %}
            <div class="col-md-4 mb-3">
                <a href="{% url 'blog:categoria' slug=categoria.slug %}" class="text-decoration-none">
                    <div class="card text-center">
                        <div class="card-body">
                            <i class="fas fa-folder fa-3x text-primary mb-3"></i>
                            <h5>{{ categoria.nome }}</h5>
                        </div>
                    </div>
                </a>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
{% endblock %}
```

### 7. CSS Personalizado

**blog/static/blog/css/style.css:**
```css
/* Reset e variáveis */
:root {
    --primary-color: #0d6efd;
    --secondary-color: #6c757d;
    --dark-color: #212529;
}

body {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

main {
    flex: 1;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, var(--primary-color) 0%, #0a58ca 100%);
}

/* Cards */
.card {
    transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

/* Footer */
footer {
    margin-top: auto;
}

footer a {
    transition: opacity 0.3s;
}

footer a:hover {
    opacity: 0.7;
}

/* Sidebar */
.sidebar {
    position: sticky;
    top: 20px;
}

/* Post Detail */
.post-meta {
    color: var(--secondary-color);
    font-size: 0.9rem;
}

.post-content {
    line-height: 1.8;
    font-size: 1.1rem;
}
```

---

## ✅ Checklist de Entrega

Verifique se seu projeto tem:

- [ ] Template base com blocos
- [ ] Navbar e footer em partials
- [ ] Herança de templates funcionando
- [ ] Uso correto de {% for %} e {% if %}
- [ ] Uso de filtros (date, truncatewords, etc)
- [ ] URLs nomeadas e namespaces
- [ ] Arquivos estáticos configurados
- [ ] Design responsivo
- [ ] 5 páginas funcionais
- [ ] Busca funcional
- [ ] requirements.txt
- [ ] README.md com instruções

---

## 🎨 Extras (Opcional)

- [ ] Paginação de posts
- [ ] Breadcrumbs
- [ ] Sidebar com posts populares
- [ ] Dark mode toggle
- [ ] Contador de visualizações
- [ ] Comentários nos posts
- [ ] Tags nos posts
- [ ] Página 404 personalizada

---

## 📊 Critérios de Avaliação

| Critério | Pontos |
|----------|--------|
| Herança de templates | 2.0 |
| Tags e filtros | 2.0 |
| Partials e includes | 1.5 |
| Arquivos estáticos | 1.5 |
| URLs e roteamento | 1.0 |
| Design e usabilidade | 1.5 |
| Código organizado | 0.5 |
| **Total** | **10.0** |

---

## 🚀 Como Executar

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install django

# Rodar servidor
python manage.py runserver

# Acessar
http://127.0.0.1:8000/
```

---

Boa sorte! 🎉
