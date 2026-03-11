# Aula 03 - Templates Django

## 🎯 Objetivos de Aprendizagem

Ao final desta aula, você será capaz de:
- Compreender o Django Template Language (DTL)
- Criar e organizar templates
- Usar herança de templates
- Trabalhar com tags e filtros
- Configurar e usar arquivos estáticos (CSS, JS, imagens)
- Criar layouts responsivos

---

## 1. O que são Templates?

**Templates** são arquivos HTML que o Django processa para gerar páginas dinâmicas. Eles permitem:
- Separar lógica de apresentação
- Reutilizar código HTML
- Inserir dados dinâmicos
- Aplicar lógica de apresentação (loops, condicionais)

---

## 2. Configurando Templates

### 2.1. Configuração no settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Templates globais
        'APP_DIRS': True,  # Busca templates dentro de cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 2.2. Estrutura de Diretórios

```
meu_projeto/
├── templates/              # Templates globais
│   └── base.html
└── blog/
    └── templates/
        └── blog/          # Namespace do app
            ├── lista.html
            └── detalhe.html
```

**Por que usar namespace?** Evita conflitos quando apps diferentes têm templates com o mesmo nome.

---

## 3. Template Básico

### 3.1. Criando um Template Simples

**blog/templates/blog/lista.html:**
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Posts</title>
</head>
<body>
    <h1>Blog</h1>
    <p>Bem-vindo ao nosso blog!</p>
</body>
</html>
```

### 3.2. Renderizando o Template

**blog/views.py:**
```python
from django.shortcuts import render

def lista_posts(request):
    return render(request, 'blog/lista.html')
```

---

## 4. Variáveis no Template

### 4.1. Passando Dados da View

**views.py:**
```python
def lista_posts(request):
    context = {
        'titulo': 'Meu Blog',
        'posts': [
            {'id': 1, 'titulo': 'Primeiro Post', 'autor': 'João'},
            {'id': 2, 'titulo': 'Segundo Post', 'autor': 'Maria'},
        ],
        'total': 2,
    }
    return render(request, 'blog/lista.html', context)
```

### 4.2. Usando Variáveis no Template

**lista.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ titulo }}</title>
</head>
<body>
    <h1>{{ titulo }}</h1>
    <p>Total de posts: {{ total }}</p>
    
    <!-- Acessar atributos -->
    {% for post in posts %}
        <h2>{{ post.titulo }}</h2>
        <p>Por: {{ post.autor }}</p>
    {% endfor %}
</body>
</html>
```

### 4.3. Notação de Ponto

```html
<!-- Atributo de objeto -->
{{ objeto.atributo }}

<!-- Chave de dicionário -->
{{ dicionario.chave }}

<!-- Índice de lista -->
{{ lista.0 }}

<!-- Método (sem parênteses) -->
{{ objeto.get_nome }}
```

---

## 5. Tags do Django

### 5.1. Tag {% if %}

```html
{% if usuario.is_authenticated %}
    <p>Bem-vindo, {{ usuario.username }}!</p>
{% else %}
    <p>Por favor, faça login.</p>
{% endif %}

<!-- Com elif -->
{% if posts %}
    <h2>Posts Disponíveis</h2>
{% elif em_manutencao %}
    <p>Site em manutenção</p>
{% else %}
    <p>Nenhum post disponível</p>
{% endif %}

<!-- Operadores -->
{% if posts|length > 5 %}
    <p>Muitos posts!</p>
{% endif %}

{% if usuario.nome == "João" %}
    <p>Olá João!</p>
{% endif %}

{% if idade >= 18 and habilitado %}
    <p>Pode dirigir</p>
{% endif %}
```

### 5.2. Tag {% for %}

```html
<!-- Loop simples -->
<ul>
    {% for post in posts %}
        <li>{{ post.titulo }}</li>
    {% endfor %}
</ul>

<!-- Com empty -->
<ul>
    {% for post in posts %}
        <li>{{ post.titulo }}</li>
    {% empty %}
        <li>Nenhum post encontrado</li>
    {% endfor %}
</ul>

<!-- Variáveis especiais do loop -->
{% for post in posts %}
    <p>
        Post {{ forloop.counter }}: {{ post.titulo }}
        {% if forloop.first %}<span class="badge">Novo!</span>{% endif %}
    </p>
{% endfor %}
```

**Variáveis do forloop:**
- `forloop.counter`: 1, 2, 3, ...
- `forloop.counter0`: 0, 1, 2, ...
- `forloop.first`: True na primeira iteração
- `forloop.last`: True na última iteração
- `forloop.parentloop`: Loop pai (em loops aninhados)

### 5.3. Tag {% url %}

```html
<!-- URL simples -->
<a href="{% url 'blog:lista' %}">Ver Posts</a>

<!-- URL com parâmetro -->
<a href="{% url 'blog:detalhe' post_id=post.id %}">{{ post.titulo }}</a>

<!-- URL com múltiplos parâmetros -->
<a href="{% url 'blog:arquivo' ano=2024 mes=3 %}">Março 2024</a>
```

### 5.4. Tag {% csrf_token %}

```html
<form method="post">
    {% csrf_token %}
    <input type="text" name="titulo">
    <button type="submit">Enviar</button>
</form>
```

### 5.5. Tag {% include %}

```html
<!-- Incluir outro template -->
{% include 'partials/navbar.html' %}

<!-- Com contexto adicional -->
{% include 'partials/card.html' with titulo="Meu Card" %}
```

### 5.6. Tag {% load %}

```html
<!-- Carregar arquivos estáticos -->
{% load static %}
<img src="{% static 'img/logo.png' %}" alt="Logo">

<!-- Carregar tags personalizadas -->
{% load custom_tags %}
```

---

## 6. Filtros do Django

### 6.1. Filtros de Texto

```html
<!-- Maiúsculas/Minúsculas -->
{{ texto|upper }}          <!-- TEXTO -->
{{ texto|lower }}          <!-- texto -->
{{ texto|title }}          <!-- Texto -->
{{ texto|capfirst }}       <!-- Primeira letra maiúscula -->

<!-- Truncar texto -->
{{ texto|truncatewords:10 }}      <!-- Primeiras 10 palavras -->
{{ texto|truncatechars:50 }}      <!-- Primeiros 50 caracteres -->

<!-- Valor padrão -->
{{ variavel|default:"Não disponível" }}
```

### 6.2. Filtros de Data e Hora

```html
<!-- Formatar data -->
{{ data|date:"d/m/Y" }}           <!-- 15/03/2026 -->
{{ data|date:"d de F de Y" }}     <!-- 15 de março de 2026 -->
{{ agora|date:"H:i" }}            <!-- 14:30 -->

<!-- Tempo relativo -->
{{ data|timesince }}              <!-- "2 dias atrás" -->
{{ data|timeuntil }}              <!-- "em 3 horas" -->
```

### 6.3. Filtros de Números

```html
<!-- Formatação -->
{{ numero|floatformat:2 }}        <!-- 10.50 -->
{{ numero|add:10 }}               <!-- Adiciona 10 -->

<!-- Lista/QuerySet -->
{{ lista|length }}                <!-- Tamanho da lista -->
{{ lista|first }}                 <!-- Primeiro item -->
{{ lista|last }}                  <!-- Último item -->
{{ lista|join:", " }}             <!-- "item1, item2, item3" -->
```

### 6.4. Filtros HTML

```html
<!-- Segurança -->
{{ texto|safe }}                  <!-- Marca HTML como seguro -->
{{ texto|escape }}                <!-- Escapa HTML -->

<!-- Links -->
{{ url|urlize }}                  <!-- Converte URLs em links -->
{{ url|urlizetrunc:30 }}          <!-- URL truncada em link -->

<!-- Linha break -->
{{ texto|linebreaks }}            <!-- \n vira <p> e <br> -->
{{ texto|linebreaksbr }}          <!-- \n vira <br> -->
```

### 6.5. Encadeando Filtros

```html
{{ texto|lower|truncatewords:5 }}
{{ valor|default:"N/A"|upper }}
{{ lista|length|add:10 }}
```

---

## 7. Herança de Templates

### 7.1. Template Base

**templates/base.html:**
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Meu Site{% endblock %}</title>
    
    <!-- CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar">
        <div class="container">
            <a href="{% url 'home' %}">Home</a>
            <a href="{% url 'blog:lista' %}">Blog</a>
            <a href="{% url 'contato' %}">Contato</a>
        </div>
    </nav>
    
    <!-- Conteúdo -->
    <main class="container">
        {% block content %}
        <!-- Conteúdo padrão aqui -->
        {% endblock %}
    </main>
    
    <!-- Footer -->
    <footer class="footer">
        <p>&copy; 2026 Meu Site. Todos os direitos reservados.</p>
    </footer>
    
    <!-- JavaScript -->
    <script src="{% static 'js/script.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### 7.2. Template Filho

**blog/templates/blog/lista.html:**
```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Blog - {{ block.super }}{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'blog/css/blog.css' %}">
{% endblock %}

{% block content %}
<h1>Posts do Blog</h1>

<div class="posts">
    {% for post in posts %}
    <article class="post-card">
        <h2>{{ post.titulo }}</h2>
        <p class="meta">Por {{ post.autor }} em {{ post.data|date:"d/m/Y" }}</p>
        <p>{{ post.resumo|truncatewords:30 }}</p>
        <a href="{% url 'blog:detalhe' post_id=post.id %}" class="btn">Ler mais</a>
    </article>
    {% empty %}
    <p>Nenhum post disponível no momento.</p>
    {% endfor %}
</div>
{% endblock %}

{% block extra_js %}
<script src="{% static 'blog/js/blog.js' %}"></script>
{% endblock %}
```

### 7.3. Usando {{ block.super }}

```html
{% block title %}
    Minha Página - {{ block.super }}  <!-- Inclui o título do pai -->
{% endblock %}
```

---

## 8. Arquivos Estáticos

### 8.1. Configuração no settings.py

```python
# URL para acessar arquivos estáticos
STATIC_URL = '/static/'

# Diretórios adicionais de arquivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Diretório onde collectstatic reúne os arquivos (produção)
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### 8.2. Estrutura de Diretórios

```
meu_projeto/
├── static/                    # Arquivos estáticos globais
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── img/
│       └── logo.png
└── blog/
    └── static/
        └── blog/             # Namespace do app
            ├── css/
            │   └── blog.css
            ├── js/
            │   └── blog.js
            └── img/
                └── banner.jpg
```

### 8.3. Usando Arquivos Estáticos

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <!-- CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <link rel="stylesheet" href="{% static 'blog/css/blog.css' %}">
</head>
<body>
    <!-- Imagens -->
    <img src="{% static 'img/logo.png' %}" alt="Logo">
    <img src="{% static 'blog/img/banner.jpg' %}" alt="Banner">
    
    <!-- JavaScript -->
    <script src="{% static 'js/script.js' %}"></script>
    <script src="{% static 'blog/js/blog.js' %}"></script>
</body>
</html>
```

### 8.4. Arquivos de Upload (Media)

**settings.py:**
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

**urls.py (projeto):**
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... suas URLs ...
]

# Apenas em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

**No template:**
```html
<!-- Arquivo de upload -->
<img src="{{ post.imagem.url }}" alt="{{ post.titulo }}">
```

---

## 9. Partials e Includes

### 9.1. Criando Partials

**templates/partials/navbar.html:**
```html
<nav class="navbar">
    <div class="container">
        <a href="{% url 'home' %}" class="logo">Meu Site</a>
        <ul class="nav-menu">
            <li><a href="{% url 'home' %}">Início</a></li>
            <li><a href="{% url 'blog:lista' %}">Blog</a></li>
            <li><a href="{% url 'sobre' %}">Sobre</a></li>
            <li><a href="{% url 'contato' %}">Contato</a></li>
        </ul>
    </div>
</nav>
```

**templates/partials/footer.html:**
```html
<footer class="footer">
    <div class="container">
        <p>&copy; 2026 Meu Site. Todos os direitos reservados.</p>
        <div class="social">
            <a href="#"><i class="fab fa-facebook"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
        </div>
    </div>
</footer>
```

### 9.2. Usando Includes

**base.html:**
```html
<body>
    {% include 'partials/navbar.html' %}
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    {% include 'partials/footer.html' %}
</body>
```

### 9.3. Includes com Contexto

**templates/partials/card.html:**
```html
<div class="card">
    <h3>{{ card_titulo }}</h3>
    <p>{{ card_descricao }}</p>
</div>
```

**Usando:**
```html
{% include 'partials/card.html' with card_titulo="Título 1" card_descricao="Descrição 1" %}
```

---

## 10. Comentários em Templates

```html
<!-- Comentário HTML (aparece no código-fonte) -->

{# Comentário Django (não aparece no código-fonte) #}

{% comment %}
Este é um comentário
de múltiplas linhas
no Django
{% endcomment %}
```

---

## 11. Exemplo Completo: Blog com Templates

### Estrutura:
```
blog/
├── templates/
│   ├── base.html
│   ├── partials/
│   │   ├── navbar.html
│   │   └── footer.html
│   └── blog/
│       ├── lista.html
│       └── detalhe.html
└── static/
    └── blog/
        ├── css/
        │   └── style.css
        └── js/
            └── script.js
```

### base.html:
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Meu Blog{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'blog/css/style.css' %}">
</head>
<body>
    {% include 'partials/navbar.html' %}
    
    <main class="container my-4">
        {% block content %}{% endblock %}
    </main>
    
    {% include 'partials/footer.html' %}
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{% static 'blog/js/script.js' %}"></script>
</body>
</html>
```

### lista.html:
```html
{% extends 'base.html' %}

{% block title %}Posts - {{ block.super }}{% endblock %}

{% block content %}
<h1 class="mb-4">Posts do Blog</h1>

<div class="row">
    {% for post in posts %}
    <div class="col-md-6 mb-4">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{{ post.titulo }}</h5>
                <p class="card-text text-muted">
                    Por {{ post.autor }} | {{ post.data|date:"d/m/Y" }}
                </p>
                <p class="card-text">{{ post.resumo|truncatewords:20 }}</p>
                <a href="{% url 'blog:detalhe' post_id=post.id %}" class="btn btn-primary">
                    Ler mais
                </a>
            </div>
        </div>
    </div>
    {% empty %}
    <div class="col-12">
        <p class="text-center">Nenhum post disponível.</p>
    </div>
    {% endfor %}
</div>
{% endblock %}
```

---

## 12. Boas Práticas

### ✅ Faça

```html
<!-- Use herança de templates -->
{% extends 'base.html' %}

<!-- Use {% load static %} -->
{% load static %}
<img src="{% static 'img/logo.png' %}">

<!-- Use URLs nomeadas -->
<a href="{% url 'blog:detalhe' post_id=post.id %}">

<!-- Use filtros para formatação -->
{{ data|date:"d/m/Y" }}

<!-- Use {% empty %} em loops -->
{% for item in lista %}
    ...
{% empty %}
    <p>Lista vazia</p>
{% endfor %}
```

### ❌ Evite

```html
<!-- Não use URLs hardcoded -->
<a href="/blog/5/">  <!-- RUIM! -->

<!-- Não esqueça {% load static %} -->
<img src="/static/img/logo.png">  <!-- RUIM! -->

<!-- Não use lógica complexa em templates -->
<!-- Faça isso na view, não no template -->

<!-- Não repita código -->
<!-- Use includes ou herança -->
```

---

## 📝 Exercícios Práticos

### Exercício 1: Sistema de Templates

1. Crie um template base (`base.html`) com:
   - Navbar
   - Área de conteúdo (block content)
   - Footer

2. Crie 3 páginas que herdam de base.html:
   - Home
   - Sobre
   - Contato

### Exercício 2: Blog Completo

1. Crie templates para:
   - Lista de posts
   - Detalhe de post
   - Formulário de novo post

2. Use:
   - Herança de templates
   - Tags {% for %} e {% if %}
   - Filtros de data e texto
   - Arquivos estáticos (CSS, JS)

### Exercício 3: Cards Reutilizáveis

1. Crie um partial `card.html`
2. Use-o com `{% include %}` passando contexto
3. Exiba uma grid de cards na home

---

## 🔗 Recursos Adicionais

- [Django Template Language](https://docs.djangoproject.com/en/5.0/ref/templates/language/)
- [Built-in Tags](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#built-in-tag-reference)
- [Built-in Filters](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#built-in-filter-reference)
- [Static Files](https://docs.djangoproject.com/en/5.0/howto/static-files/)

---

## 📚 Próxima Aula

Na **Aula 04**, você aprenderá:
- Integrar JavaScript com Django
- AJAX e requisições assíncronas
- Fetch API
- Criar interfaces dinâmicas

---

**Continue praticando e nos vemos na próxima aula!** 🚀
