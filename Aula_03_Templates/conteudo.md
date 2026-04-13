# Aula 03 - Templates no Django

## 📋 Objetivos da Aula

Ao final desta aula, você será capaz de:
- Entender o sistema de templates do Django
- Criar e organizar templates HTML
- Usar variáveis para exibir dados dinâmicos
- Implementar herança de templates para reutilizar código
- Usar as tags principais: `{% if %}`, `{% for %}`, `{% url %}`
- Trabalhar com arquivos estáticos (CSS, JS, imagens)
- Passar dados fictícios das views para os templates

---

## 1. O que são Templates?

**Templates** são arquivos HTML que o Django processa para gerar páginas dinâmicas. Eles permitem:
- Separar a lógica de negócio da apresentação
- Reutilizar código HTML
- Inserir dados dinâmicos vindos das views
- Aplicar lógica de apresentação (loops, condicionais)

O Django usa o **Django Template Language (DTL)** - uma linguagem simples e poderosa para criar templates.

> **Importante:** Nesta aula trabalharemos apenas com templates e dados fictícios passados via contexto (dicionários e listas). Não utilizaremos banco de dados ainda.

---

## 2. Configurando Templates

### 2.1. Estrutura de Diretórios

```
mercado/                    # Projeto principal
├── templates/              # Templates globais
│   └── base.html
└── produtos/               # App
    └── templates/
        └── produtos/       # Namespace do app
            ├── lista.html
            └── detalhe.html
```

**Por que usar namespace (produtos/)?** Para evitar conflitos quando apps diferentes têm templates com o mesmo nome.

### 2.2. Configuração no settings.py

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

---

## 3. Template Básico e Variáveis

### 3.1. Criando um Template Simples

**produtos/templates/produtos/lista.html:**
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Produtos</title>
</head>
<body>
    <h1>Produtos do Mercado</h1>
    <p>Bem-vindo ao sistema de gerenciamento!</p>
</body>
</html>
```

### 3.2. Passando Dados da View

**produtos/views.py:**
```python
from django.shortcuts import render

def lista_produtos(request):
    # Dados fictícios passados via contexto
    contexto = {
        'titulo': 'Lista de Produtos',
        'produtos': [
            {'nome': 'Arroz 5kg', 'preco': 25.90, 'estoque': 150},
            {'nome': 'Feijão 1kg', 'preco': 8.50, 'estoque': 200},
            {'nome': 'Açúcar 1kg', 'preco': 4.99, 'estoque': 120},
        ],
        'total_produtos': 3
    }
    return render(request, 'produtos/lista.html', contexto)
```

### 3.3. Usando Variáveis no Template

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ titulo }}</title>
</head>
<body>
    <h1>{{ titulo }}</h1>
    <p>Total de produtos: {{ total_produtos }}</p>
</body>
</html>
```

**Sintaxe de variável:** `{{ nome_da_variavel }}`

### 3.4. Acessando Dados com Notação de Ponto

```html
<!-- Acessar chave de dicionário -->
<p>{{ produto.nome }}</p>
<p>R$ {{ produto.preco }}</p>
<p>Estoque: {{ produto.estoque }} unidades</p>

<!-- Acessar índice de lista -->
<p>Primeiro produto: {{ produtos.0.nome }}</p>
<p>Segundo produto: {{ produtos.1.nome }}</p>
```

---

## 4. Herança de Templates

A herança permite criar um template base com a estrutura comum e reutilizá-lo em várias páginas.

### 4.1. Criando o Template Base

**templates/base.html:**
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Sistema de Mercado{% endblock %}</title>
    
    <!-- CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Sidebar -->
    <nav class="sidebar">
        <h2>Mercado</h2>
        <ul>
            <li><a href="{% url 'home' %}">Dashboard</a></li>
            <li><a href="{% url 'produtos:lista' %}">Produtos</a></li>
            <li><a href="{% url 'vendas:lista' %}">Vendas</a></li>
            <li><a href="{% url 'clientes:lista' %}">Clientes</a></li>
        </ul>
    </nav>
    
    <!-- Conteúdo Principal -->
    <main class="content">
        <header>
            <h1>{% block header %}Dashboard{% endblock %}</h1>
        </header>
        
        {% block content %}
        <!-- Conteúdo específico de cada página -->
        {% endblock %}
    </main>
    
    <!-- JavaScript -->
    <script src="{% static 'js/style.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

**Conceitos importantes:**
- `{% block nome_do_bloco %}...{% endblock %}`: Define áreas que podem ser substituídas
- `{% load static %}`: Carrega a funcionalidade de arquivos estáticos
- `{% static 'caminho/arquivo' %}`: Referencia arquivos CSS, JS, imagens

### 4.2. Herdando do Template Base

**produtos/templates/produtos/lista.html:**
```html
{% extends 'base.html' %}

{% block title %}Produtos - {{ block.super }}{% endblock %}

{% block header %}Lista de Produtos{% endblock %}

{% block content %}
<div class="produtos-container">
    <h2>Produtos Disponíveis</h2>
    
    <!-- Aqui vamos usar as tags para exibir os produtos -->
    <p>Total: {{ total_produtos }} produtos</p>
</div>
{% endblock %}
```

**Conceitos importantes:**
- `{% extends 'base.html' %}`: **Deve ser a primeira linha** do template
- `{% block nome %}`: Substitui o conteúdo do bloco definido no base
- `{{ block.super }}`: Inclui o conteúdo do bloco pai (opcional)

---

## 5. Tags Principais do Django

### 5.1. Tag {% if %} - Condicionais

Use `{% if %}` para exibir conteúdo condicionalmente.

**Sintaxe básica:**
```html
{% if condicao %}
    <p>Conteúdo exibido se a condição for verdadeira</p>
{% endif %}
```

**Com else:**
```html
{% if usuario.is_authenticated %}
    <p>Bem-vindo, {{ usuario.nome }}!</p>
{% else %}
    <p>Por favor, faça login.</p>
{% endif %}
```

**Com elif:**
```html
{% if produtos %}
    <h2>Produtos Disponíveis</h2>
{% elif em_manutencao %}
    <p>Sistema em manutenção</p>
{% else %}
    <p>Nenhum produto cadastrado</p>
{% endif %}
```

**Operadores disponíveis:**
```html
<!-- Comparação -->
{% if estoque > 10 %}
    <span class="badge-success">Em estoque</span>
{% endif %}

{% if estoque < 5 %}
    <span class="badge-warning">Estoque baixo!</span>
{% endif %}

{% if produto.preco == 0 %}
    <span class="badge-info">Grátis</span>
{% endif %}

<!-- Lógicos -->
{% if idade >= 18 and habilitado %}
    <p>Pode dirigir</p>
{% endif %}

{% if promocao or desconto %}
    <span class="badge-sale">Oferta!</span>
{% endif %}

<!-- Negação -->
{% if not esgotado %}
    <button>Adicionar ao carrinho</button>
{% endif %}
```

### 5.2. Tag {% for %} - Loops

Use `{% for %}` para percorrer listas e exibir dados repetidos.

**Sintaxe básica:**
```html
<ul>
    {% for produto in produtos %}
        <li>{{ produto.nome }} - R$ {{ produto.preco }}</li>
    {% endfor %}
</ul>
```

**Com {% empty %}:**
```html
<ul>
    {% for produto in produtos %}
        <li>{{ produto.nome }} - R$ {{ produto.preco }}</li>
    {% empty %}
        <li>Nenhum produto encontrado</li>
    {% endfor %}
</ul>
```

**Variáveis especiais do loop (forloop):**
```html
{% for produto in produtos %}
    <div class="produto-card">
        <span class="numero">{{ forloop.counter }}</span>
        <h3>{{ produto.nome }}</h3>
        
        {% if forloop.first %}
            <span class="badge">Destaque</span>
        {% endif %}
        
        {% if forloop.last %}
            <span class="badge">Último</span>
        {% endif %}
    </div>
{% endfor %}
```

**Variáveis do forloop:**
- `forloop.counter`: 1, 2, 3, ... (começa em 1)
- `forloop.counter0`: 0, 1, 2, ... (começa em 0)
- `forloop.first`: `True` na primeira iteração
- `forloop.last`: `True` na última iteração

### 5.3. Tag {% url %} - URLs Nomeadas

Use `{% url %}` para gerar URLs baseadas nos nomes definidos no `urls.py`.

**URLs simples:**
```html
<a href="{% url 'home' %}">Dashboard</a>
<a href="{% url 'produtos:lista' %}">Ver Produtos</a>
```

**URLs com parâmetros:**
```html
<!-- Com um parâmetro -->
<a href="{% url 'produtos:detalhe' produto_id=5 %}">Ver detalhes</a>

<!-- Com múltiplos parâmetros -->
<a href="{% url 'vendas:relatorio' ano=2024 mes=3 %}">Relatório Março/2024</a>
```

**Vantagem:** Se você mudar a URL no `urls.py`, os templates são atualizados automaticamente!

### 5.4. Tag {% load static %} - Arquivos Estáticos

Use `{% load static %}` no início do template para poder carregar arquivos CSS, JS e imagens.

```html
{% load static %}

<!-- CSS -->
<link rel="stylesheet" href="{% static 'css/style.css' %}">

<!-- JavaScript -->
<script src="{% static 'js/style.js' %}"></script>

<!-- Imagens -->
<img src="{% static 'img/logo.png' %}" alt="Logo">
<img src="{% static 'img/profile.png' %}" alt="Perfil">
```

---

## 6. Arquivos Estáticos

### 6.1. Configuração no settings.py

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

### 6.2. Estrutura de Diretórios

```
mercado/
├── static/                  # Arquivos estáticos globais
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── style.js
│   └── img/
│       ├── logo.png
│       └── profile.png
└── produtos/
    └── static/
        └── produtos/        # Namespace do app
            ├── css/
            │   └── produtos.css
            └── js/
                └── produtos.js
```

---

## 7. Exemplo Completo

### 7.1. View com Dados Fictícios

**views.py:**
```python
from django.shortcuts import render

def home(request):
    contexto = {
        'page_title': 'Dashboard',
        'user_name': 'Maria Silva',
        'estatisticas': [
            {'label': 'Total de Produtos', 'value': 150},
            {'label': 'Vendas Hoje', 'value': 42},
            {'label': 'Clientes Ativos', 'value': 328},
        ],
        'produtos_destaque': [
            {'nome': 'Arroz 5kg', 'preco': 25.90, 'estoque': 150},
            {'nome': 'Feijão 1kg', 'preco': 8.50, 'estoque': 200},
            {'nome': 'Açúcar 1kg', 'preco': 4.99, 'estoque': 120},
        ]
    }
    return render(request, 'home.html', contexto)
```

### 7.2. Template com Herança e Tags

**home.html:**
```html
{% extends 'base.html' %}
{% load static %}

{% block title %}{{ page_title }} - {{ block.super }}{% endblock %}

{% block content %}
<div class="dashboard">
    <!-- Estatísticas -->
    <div class="stats-grid">
        {% for stat in estatisticas %}
        <div class="stat-card">
            <h3>{{ stat.value }}</h3>
            <p>{{ stat.label }}</p>
        </div>
        {% endfor %}
    </div>
    
    <!-- Produtos em Destaque -->
    <div class="produtos-destaque">
        <h2>Produtos em Destaque</h2>
        
        {% if produtos_destaque %}
        <div class="produtos-grid">
            {% for produto in produtos_destaque %}
            <div class="produto-card">
                <h3>{{ produto.nome }}</h3>
                <p class="preco">R$ {{ produto.preco }}</p>
                
                {% if produto.estoque < 10 %}
                    <span class="badge-warning">Estoque baixo!</span>
                {% else %}
                    <span class="badge-success">Disponível</span>
                {% endif %}
                
                <p>Estoque: {{ produto.estoque }} un.</p>
                
                {% if forloop.first %}
                    <span class="badge-star">⭐ Mais vendido</span>
                {% endif %}
            </div>
            {% endfor %}
        </div>
        {% else %}
        <p>Nenhum produto em destaque no momento.</p>
        {% endif %}
    </div>
</div>
{% endblock %}
```

---

## 8. Boas Práticas

### ✅ Faça

```html
<!-- Use herança de templates -->
{% extends 'base.html' %}

<!-- Carregue static no início -->
{% load static %}

<!-- Use URLs nomeadas -->
<a href="{% url 'produtos:lista' %}">Produtos</a>

<!-- Use {% empty %} em loops -->
{% for item in lista %}
    {{ item }}
{% empty %}
    <p>Lista vazia</p>
{% endfor %}

<!-- Use if para mensagens condicionais -->
{% if estoque < 5 %}
    <span>Estoque baixo!</span>
{% endif %}
```

### ❌ Evite

```html
<!-- Não use URLs fixas -->
<a href="/produtos/">  <!-- RUIM! -->

<!-- Não esqueça {% load static %} -->
<img src="/static/img/logo.png">  <!-- RUIM! -->

<!-- Não use lógica complexa em templates -->
<!-- Faça cálculos na view, não no template -->

<!-- Não repita código -->
<!-- Use herança ao invés de copiar/colar -->
```

---

## 9. Exercícios Práticos

### Exercício 1: Template Base

1. Crie um template base (`base.html`) com:
   - Cabeçalho com logo e menu
   - Área de conteúdo usando `{% block content %}`
   - Rodapé
   - Carregamento de CSS e JS

2. Crie 2 páginas que herdam do base:
   - Dashboard (home)
   - Lista de Produtos

### Exercício 2: Usando Tags

1. Na view, crie uma lista de 5 produtos fictícios com nome, preço e estoque

2. No template:
   - Use `{% for %}` para exibir todos os produtos
   - Use `{% if %}` para mostrar uma badge de "Estoque baixo" quando estoque < 10
   - Use `forloop.counter` para numerar os produtos

### Exercício 3: Dashboard com Estatísticas

1. Crie uma view que passa:
   - Lista com 3 estatísticas (ex: total de produtos, vendas do dia, clientes)
   - Lista de produtos recentes

2. No template:
   - Use `{% for %}` para exibir cards de estatísticas
   - Use `{% if %}` com `{% empty %}` para produtos recentes
   - Mostre uma mensagem diferente se não houver produtos

> **Dica:** Consulte o arquivo `projeto_pratico.md` para exercícios completos com soluções!

---

## 10. Resumo

Nesta aula aprendemos:

✅ **Templates** são arquivos HTML que o Django processa  
✅ Usar **variáveis** com `{{ variavel }}` para dados dinâmicos  
✅ **Herança de templates** com `{% extends %}` e `{% block %}` para reutilizar código  
✅ Tag **{% if %}** para condicionais  
✅ Tag **{% for %}** para loops  
✅ Tag **{% url %}** para gerar URLs  
✅ Tag **{% load static %}** e **{% static %}** para arquivos CSS/JS/imagens  
✅ Passar **dados fictícios** das views via contexto

---

## 🔗 Recursos Adicionais

- [Django Template Language - Documentação Oficial](https://docs.djangoproject.com/en/5.0/ref/templates/language/)
- [Built-in Tags - Django](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#built-in-tag-reference)
- [Static Files - Django](https://docs.djangoproject.com/en/5.0/howto/static-files/)

---

## 📚 Próxima Aula

Na **Aula 04**, você aprenderá:
- Integrar JavaScript com Django
- Criar interatividade nas páginas
- Manipular o DOM
- Fetch API para requisições

---

**Continue praticando! 🚀**
