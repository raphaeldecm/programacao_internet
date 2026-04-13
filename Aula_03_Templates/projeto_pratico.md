# Projeto Prático 3 - Dashboard de Mercado com Templates

## 🎯 Objetivo

Praticar Django Template Language através de exercícios progressivos focados em:
- Herança de templates ({% extends %}, {% block %})
- Tags de controle ({% if %}, {% for %})
- Filtros do Django
- Passagem de dados fictícios por contexto
- Organização de templates

**Nota:** Neste projeto, vamos trabalhar apenas com dados fictícios passados via contexto. Não abordaremos models, banco de dados ou operações CRUD neste momento.

---

## 📋 Exercícios Práticos

### Exercício 1: Template Base e Herança

**Objetivo:** Criar um template base e aplicar herança

**Tarefa:**
1. Crie um `base.html` com:
   - Estrutura HTML básica
   - Bloco para título ({% block title %})
   - Bloco para conteúdo ({% block content %})
   - Bloco para scripts extras ({% block extra_js %})

2. Crie `home.html` que herda de base.html:
   - Use {% extends 'base.html' %}
   - Defina um título personalizado
   - Adicione conteúdo simples

**Dica de implementação:**
```python
# views.py
def home(request):
    return render(request, 'home.html')
```

---

### Exercício 2: Passando Dados por Contexto

**Objetivo:** Entender como passar dados da view para o template

**Tarefa:**
Crie uma view que passa dados fictícios de produtos para o template:

```python
# produtos/views.py
def lista_produtos(request):
    produtos = [
        {'nome': 'Arroz 1kg', 'preco': 12.50, 'estoque': 150},
        {'nome': 'Feijão 1kg', 'preco': 8.90, 'estoque': 200},
        {'nome': 'Macarrão 500g', 'preco': 4.50, 'estoque': 80},
    ]
    
    context = {
        'produtos': produtos,
        'total': len(produtos),
    }
    return render(request, 'produtos/lista.html', context)
```

No template, exiba:
- O total de produtos
- Uma mensagem de boas-vindas

---

### Exercício 3: Loop com {% for %}

**Objetivo:** Iterar sobre uma lista de dados

**Tarefa:**
No template `produtos/lista.html`, use {% for %} para:

1. Listar todos os produtos
2. Exibir nome, preço e estoque de cada um
3. Usar {% empty %} para caso não haja produtos

**Exemplo de estrutura:**
```html
<h1>Produtos Disponíveis</h1>
<p>Total: {{ total }}</p>

<div class="produtos-grid">
    {% for produto in produtos %}
        <!-- Exibir produto aqui -->
    {% empty %}
        <p>Nenhum produto disponível.</p>
    {% endfor %}
</div>
```

---

### Exercício 4: Condicionais com {% if %}

### Exercício 4: Condicionais com {% if %}

**Objetivo:** Aplicar lógica condicional nos templates

**Tarefa:**
Modifique a listagem de produtos para:

1. Mostrar badge "Estoque Baixo" se estoque < 100
2. Mostrar badge "Disponível" se estoque >= 100
3. Aplicar classe CSS diferente para cada caso

**Exemplo:**
```html
{% for produto in produtos %}
    <div class="produto-card">
        <h3>{{ produto.nome }}</h3>
        <p>R$ {{ produto.preco }}</p>
        <p>Estoque: {{ produto.estoque }}</p>
        
        {% if produto.estoque < 100 %}
            <span class="badge badge-warning">Estoque Baixo</span>
        {% else %}
            <span class="badge badge-success">Disponível</span>
        {% endif %}
    </div>
{% endfor %}
```

---

### Exercício 5: Filtros do Django

**Objetivo:** Usar filtros para formatar dados

**Tarefa:**
Na listagem de produtos, use filtros para:

1. Formatar preços com 2 casas decimais: `{{ produto.preco|floatformat:2 }}`
2. Converter nome para maiúsculas: `{{ produto.nome|upper }}`
3. Adicionar unidade ao estoque: `{{ produto.estoque }} un.`

**Dados adicionais para teste:**
```python
from datetime import datetime

produtos = [
    {
        'nome': 'Arroz 1kg', 
        'preco': 12.5, 
        'estoque': 150,
        'data_cadastro': datetime(2024, 3, 15),
    },
    # ... mais produtos
]
```

Use o filtro `date` para formatar data:
```html
<p>Cadastrado em: {{ produto.data_cadastro|date:"d/m/Y" }}</p>
```

---

###Exercício 6: Variáveis do Loop (forloop)

**Objetivo:** Usar variáveis especiais do loop

**Tarefa:**
Modifique a listagem para:

1. Numerar os produtos usando `{{ forloop.counter }}`
2. Marcar o primeiro produto como "Destaque" usando `{% if forloop.first %}`
3. Aplicar classe especial ao último produto usando `{% if forloop.last %}`  

**Exemplo:**
```html
{% for produto in produtos %}
    <div class="produto-card {% if forloop.first %}destaque{% endif %}">
        <span class="numero">{{ forloop.counter }}</span>
        <h3>{{ produto.nome }}</h3>
        
        {% if forloop.first %}
            <span class="badge badge-primary">Destaque!</span>
        {% endif %}
    </div>
{% endfor %}
```

---

### Exercício 7: Trabalhando com Categorias

**Objetivo:** Filtrar dados baseado em categorias

**Tarefa:**
Crie uma view que passa produtos organizados por categoria:

```python
def lista_por_categoria(request):
    produtos = [
        {'nome': 'Arroz', 'preco': 12.50, 'categoria': 'Alimentos'},
        {'nome': 'Feijão', 'preco': 8.90, 'categoria': 'Alimentos'},
        {'nome': 'Refrigerante', 'preco': 7.50, 'categoria': 'Bebidas'},
        {'nome': 'Água', 'preco': 2.00, 'categoria': 'Bebidas'},
    ]
    
    context = {
        'produtos': produtos,
        'categorias': ['Alimentos', 'Bebidas'],
    }
    return render(request, 'produtos/por_categoria.html', context)
```

No template, agrupe produtos por categoria usando loops aninhados:

```html
{% for categoria in categorias %}
    <h2>{{ categoria }}</h2>
    <div class="produtos-grid">
        {% for produto in produtos %}
            {% if produto.categoria == categoria %}
                <!-- Exibir produto -->
            {% endif %}
        {% endfor %}
    </div>
{% endfor %}
```

---

### Exercício 8: Dashboard com Estatísticas

**Objetivo:** Criar um dashboard com dados agregados

**Tarefa:**
Crie uma view `dashboard` que calcula estatísticas:

```python
def dashboard(request):
    produtos = [
        {'nome': 'Arroz', 'preco': 12.50, 'estoque': 150},
        {'nome': 'Feijão', 'preco': 8.90, 'estoque': 200},
        {'nome': 'Macarrão', 'preco': 4.50, 'estoque': 45},
    ]
    
    # Calcular estatísticas
    total_produtos = len(produtos)
    produtos_baixo_estoque = len([p for p in produtos if p['estoque'] < 100])
    valor_total_estoque = sum(p['preco'] * p['estoque'] for p in produtos)
    
    context = {
        'total_produtos': total_produtos,
        'produtos_baixo_estoque': produtos_baixo_estoque,
        'valor_total_estoque': valor_total_estoque,
        'produtos': produtos,
    }
    return render(request, 'dashboard.html', context)
```

No template:
- Exiba os cards com as estatísticas
- Liste apenas produtos com estoque baixo
- Use cores diferentes para alertas (vermelho se houver produtos com estoque baixo)

---

### Exercício 9: Template com Includes (Partial)

**Objetivo:** Reutilizar componentes de template

**Tarefa:**
1. Crie um partial `produtos/_card.html`:

```html
<!-- produtos/templates/produtos/_card.html -->
<div class="produto-card">
    <h3>{{ produto.nome }}</h3>
    <p class="preco">R$ {{ produto.preco|floatformat:2 }}</p>
    <p class="estoque">
        Estoque: {{ produto.estoque }} un.
        {% if produto.estoque < 100 %}
            <span class="badge-warning">Baixo</span>
        {% endif %}
    </p>
</div>
```

2. Use o partial na listagem:

```html
<!-- produtos/templates/produtos/lista.html -->
<div class="produtos-grid">
    {% for produto in produtos %}
        {% include 'produtos/_card.html' %}
    {% endfor %}
</div>
```

---

### Exercício 10: Últimas Transações

**Objetivo:** Trabalhar com tabelas e dados temporais

**Tarefa:**
Crie uma view que exibe últimas transações:

```python
from datetime import datetime, timedelta

def ultimas_transacoes(request):
    transacoes = [
        {
            'id': 1001,
            'cliente': 'João Silva',
            'produto': 'Arroz 1kg',
            'valor': 12.50,
            'data': datetime.now() - timedelta(hours=2),
            'status': 'concluido'
        },
        {
            'id': 1002,
            'cliente': 'Maria Santos',
            'produto': 'Feijão 1kg',
            'valor': 8.90,
            'data': datetime.now() - timedelta(hours=5),
            'status': 'pendente'
        },
        {
            'id': 1003,
            'cliente': 'Pedro Costa',
            'produto': 'Macarrão 500g',
            'valor': 4.50,
            'data': datetime.now() - timedelta(days=1),
            'status': 'cancelado'
        },
    ]
    
    context = {'transacoes': transacoes}
    return render(request, 'transacoes.html', context)
```

No template, crie uma tabela que:
- Exibe todas as transações
- Usa badge com cores diferentes para cada status
- Formata a data com `timesince` filter: `{{ transacao.data|timesince }} atrás`
- Aplica classe CSS diferente para cada status

**Exemplo:**
```html
<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Cliente</th>
            <th>Produto</th>
            <th>Valor</th>
            <th>Quando</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        {% for transacao in transacoes %}
        <tr>
            <td>#{{ transacao.id }}</td>
            <td>{{ transacao.cliente }}</td>
            <td>{{ transacao.produto }}</td>
            <td>R$ {{ transacao.valor|floatformat:2 }}</td>
            <td>{{ transacao.data|timesince }} atrás</td>
            <td>
                {% if transacao.status == 'concluido' %}
                    <span class="badge-success">Concluído</span>
                {% elif transacao.status == 'pendente' %}
                    <span class="badge-warning">Pendente</span>
                {% else %}
                    <span class="badge-danger">Cancelado</span>
                {% endif %}
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

---

## 🗂️ Estrutura Sugerida do Projeto

```
Projeto/
├── mercado/
│   ├── settings.py
│   └── urls.py
├── produtos/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── produtos/
│           ├── lista.html
│           ├── por_categoria.html
│           └── _card.html       # Partial
├── templates/
│   ├── base.html                # Template base
│   ├── home.html
│   ├── dashboard.html
│   └── transacoes.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── manage.py
```

---

## ✅ Checklist de Conceitos

Certifique-se de que praticou:

- [ ] Herança de templates com {% extends %}
- [ ] Definição e uso de {% block %}
- [ ] Loop com {% for %} e {% empty %}
- [ ] Condicionais com {% if %}, {% elif %}, {% else %}
- [ ] Variáveis do forloop (counter, first, last)
- [ ] Filtros básicos (floatformat, date, upper, lower)
- [ ] Filtro timesince para datas
- [ ] {% include %} para partials
- [ ] Passagem de dados por contexto
- [ ] Notação de ponto para acessar atributos
- [ ] Comparações em templates (==, <, >, <=, >=)
- [ ] Operadores lógicos (and, or, not)

---

## 📚 Desafios Extras

### Desafio 1: Menu de Navegação Dinâmico
Crie um menu que destaca a página ativa usando {% if request.path == '/produtos/' %}

### Desafio 2: Busca de Produtos
Implemente uma busca simples que filtra produtos pelo nome passado via GET

### Desafio 3: Ordenação
Adicione botões para ordenar produtos por preço (crescente/decrescente)

### Desafio 4: Paginação Manual  
Divida uma lista grande em "páginas" de 5 itens usando slicing: `produtos|slice:":5"`

### Desafio 5: Contador de Visualizações
Simule um contador usando variáveis no contexto e exiba com formatação: `{{ views|intcomma }}`

---

## 🎯 Dicas de Implementação

### Configuração Básica de URLs

**mercado/urls.py:**
```python
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('produtos/', include('produtos.urls')),
]
```

**produtos/urls.py:**
```python
from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transacoes/', views.ultimas_transacoes, name='transacoes'),
]
```

### Template Base Mínimo

```html
<!-- templates/base.html -->
{% load static %}
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Mercado{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'produtos:lista' %}">Produtos</a>
        <a href="{% url 'produtos:dashboard' %}">Dashboard</a>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <script src="{% static 'js/script.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

## 📖 Resumo dos Filtros Mais Usados

| Filtro | Exemplo | Resultado |
|--------|---------|-----------|
| `floatformat:2` | `{{ 12.5\|floatformat:2 }}` | 12.50 |
| `date:"d/m/Y"` | `{{ data\|date:"d/m/Y" }}` | 15/03/2024 |
| `timesince` | `{{ data\|timesince }}` | 2 horas |
| `upper` | `{{ "texto"\|upper }}` | TEXTO |
| `lower` | `{{ "TEXTO"\|lower }}` | texto |
| `truncatewords:10` | `{{ texto\|truncatewords:10 }}` | Primeiras 10 palavras... |
| `default:"N/A"` | `{{ variavel\|default:"N/A" }}` | N/A (se vazio) |
| `length` | `{{ lista\|length }}` | 5 |

---

## 🚀 Como Começar

1. **Crie o projeto Django:**
```bash
django-admin startproject mercado .
python manage.py startapp produtos
```

2. **Configure TEMPLATES em settings.py:**
```python
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

3. **Crie os diretórios:**
```bash
mkdir -p templates produtos/templates/produtos static/css static/js
```

4. **Comece pelo Exercício 1** e vá progredindo!

---

Bons estudos! 📚✨
### 4. Criar Dashboard Principal (Home)

**templates/home.html:**
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mercado Dashboard</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <!-- Sidebar -->
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="logo">
                <div class="logo-icon">M</div>
                <span>Mercado</span>
            </div>
        </div>
        <nav>
            <ul class="nav-menu">
                <li class="nav-item">
                    <a href="{% url 'home' %}" class="nav-link active">
                        <span class="nav-icon">📊</span>
                        <span>Dashboard</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="{% url 'produtos:lista' %}" class="nav-link">
                        <span class="nav-icon">📦</span>
                        <span>Produtos</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <span class="nav-icon">👥</span>
                        <span>Clientes</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <span class="nav-icon">💰</span>
                        <span>Vendas</span>
                    </a>
                </li>
            </ul>
        </nav>
    </aside>

    <!-- Main Content -->
    <main class="main-content">
        <!-- Header -->
        <header class="header">
            <div class="header-left">
                <h1>Dashboard</h1>
                <p class="header-subtitle">Bem-vindo ao painel de controle</p>
            </div>
            <div class="header-right">
                <div class="user-info">
                    <div class="user-avatar">
                        <img src="{% static 'img/profile.png' %}" alt="Avatar">
                    </div>
                    <div class="user-details">
                        <span class="user-name">Administrador</span>
                        <span class="user-role">Admin</span>
                    </div>
                </div>
                <button class="btn btn-outline">Sair</button>
            </div>
        </header>

        <!-- Stats Grid -->
        <div class="container">
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-header">
                        <div>
                            <div class="stat-value">1,247</div>
                            <div class="stat-label">Produtos</div>
                        </div>
                        <div class="stat-icon products">📦</div>
                    </div>
                    <div class="stat-change positive">↑ 12% este mês</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-header">
                        <div>
                            <div class="stat-value">R$ 45.8k</div>
                            <div class="stat-label">Vendas</div>
                        </div>
                        <div class="stat-icon sales">💰</div>
                    </div>
                    <div class="stat-change positive">↑ 23% este mês</div>
                </div>
                
                <!-- Adicionar mais cards... -->
            </div>

            <!-- Charts -->
            <div class="charts-grid">
                <div class="chart-card">
                    <div class="card-header">
                        <h2 class="card-title">Vendas Mensais</h2>
                    </div>
                    <div class="chart-placeholder">
                        <canvas id="salesCanvas"></canvas>
                    </div>
                </div>
            </div>

            <!-- Transactions Table -->
            <div class="table-card">
                <div class="card-header">
                    <h2 class="card-title">Últimas Transações</h2>
                    <button class="btn btn-primary">Ver Todas</button>
                </div>
                <div class="table-responsive">
                    <table>
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Cliente</th>
                                <th>Produto</th>
                                <th>Valor</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Dados da tabela -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </main>

    <script src="{% static 'js/style.js' %}"></script>
</body>
</html>
```

### 5. Criar Lista de Produtos

**produtos/templates/produtos/lista.html:**
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Produtos - Mercado</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <!-- Sidebar -->
    <!-- (Mesmo sidebar do dashboard) -->

    <!-- Main Content -->
    <main class="main-content">
        <header class="header">
            <div class="header-left">
                <h1>Produtos</h1>
                <p class="header-subtitle">{{ total }} produto{{ total|pluralize }} encontrado{{ total|pluralize }}</p>
            </div>
            <div class="header-right">
                <a href="{% url 'produtos:novo' %}" class="btn btn-primary">+ Novo Produto</a>
            </div>
        </header>

        <div class="container">
            <!-- Filtros -->
            <div class="filters-bar">
                <form method="get" action="{% url 'produtos:buscar' %}">
                    <input type="search" name="q" placeholder="Buscar produtos...">
                    <button type="submit">Buscar</button>
                </form>

                <div class="category-filter">
                    <a href="{% url 'produtos:lista' %}" 
                       class="badge {% if not request.GET.categoria %}active{% endif %}">
                        Todas
                    </a>
                    {% for categoria in categorias %}
                    <a href="{% url 'produtos:categoria' slug=categoria.slug %}"
                       class="badge">
                        {{ categoria.nome }}
                    </a>
                    {% endfor %}
                </div>
            </div>

            <!-- Grid de Produtos -->
            <div class="products-grid">
                {% for produto in produtos %}
                <div class="product-card">
                    <div class="product-image">
                        <img src="{% static produto.imagem %}" alt="{{ produto.nome }}">
                    </div>
                    <div class="product-body">
                        <span class="badge">{{ produto.categoria }}</span>
                        <h3>{{ produto.nome }}</h3>
                        <p class="price">R$ {{ produto.preco|floatformat:2 }}</p>
                        <p class="stock">
                            Estoque: {{ produto.estoque }} un.
                            {% if produto.estoque < 50 %}
                            <span class="badge badge-warning">Baixo</span>
                            {% endif %}
                        </p>
                        <div class="product-actions">
                            <a href="{% url 'produtos:detalhe' produto_id=produto.id %}" 
                               class="btn btn-outline">Ver Detalhes</a>
                        </div>
                    </div>
                </div>
                {% empty %}
                <div class="empty-state">
                    <p>Nenhum produto encontrado.</p>
                </div>
                {% endfor %}
            </div>
        </div>
    </main>

    <script src="{% static 'js/style.js' %}"></script>
</body>
</html>
```

### 6. Criar Detalhe do Produto

**produtos/templates/produtos/detalhe.html:**
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{{ produto.nome }} - Mercado</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <!-- Sidebar -->
    
    <main class="main-content">
        <header class="header">
            <div class="header-left">
                <a href="{% url 'produtos:lista' %}" class="btn btn-outline">← Voltar</a>
                <h1>{{ produto.nome }}</h1>
            </div>
            <div class="header-right">
                <a href="{% url 'produtos:editar' produto_id=produto.id %}" 
                   class="btn btn-primary">Editar</a>
            </div>
        </header>

        <div class="container">
            <div class="product-detail">
                <div class="product-image-large">
                    <img src="{% static produto.imagem %}" alt="{{ produto.nome }}">
                </div>
                
                <div class="product-info">
                    <span class="badge">{{ produto.categoria }}</span>
                    <h2>{{ produto.nome }}</h2>
                    <p class="price-large">R$ {{ produto.preco|floatformat:2 }}</p>
                    
                    <div class="info-grid">
                        <div class="info-item">
                            <span class="label">Estoque:</span>
                            <span class="value">{{ produto.estoque }} unidades</span>
                        </div>
                        <div class="info-item">
                            <span class="label">Status:</span>
                            <span class="value">{{ produto.status|upper }}</span>
                        </div>
                        <div class="info-item">
                            <span class="label">Cadastrado em:</span>
                            <span class="value">{{ produto.data_cadastro|date:"d/m/Y" }}</span>
                        </div>
                    </div>
                    
                    <div class="description">
                        <h3>Descrição</h3>
                        <p>{{ produto.descricao }}</p>
                    </div>

                    <form method="post" action="{% url 'produtos:excluir' produto_id=produto.id %}">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-danger" 
                                onclick="return confirm('Tem certeza?')">
                            Excluir Produto
                        </button>
                    </form>
                </div>
            </div>

            <!-- Produtos Relacionados -->
            {% if produtos_relacionados %}
            <section class="related-products">
                <h2>Produtos Relacionados</h2>
                <div class="products-grid">
                    {% for relacionado in produtos_relacionados %}
                    <div class="product-card">
                        <div class="product-image">
                            <img src="{% static relacionado.imagem %}" alt="{{ relacionado.nome }}">
                        </div>
                        <div class="product-body">
                            <h3>{{ relacionado.nome }}</h3>
                            <p class="price">R$ {{ relacionado.preco|floatformat:2 }}</p>
                            <a href="{% url 'produtos:detalhe' produto_id=relacionado.id %}" 
                               class="btn btn-outline">Ver</a>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </section>
            {% endif %}
        </div>
    </main>

    <script src="{% static 'js/style.js' %}"></script>
</body>
</html>
```

### 7. Criar Formulário de Produto

**produtos/templates/produtos/form.html:**
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{% if edicao %}Editar{% else %}Novo{% endif %} Produto - Mercado</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <!-- Sidebar -->

    <main class="main-content">
        <header class="header">
            <div class="header-left">
                <a href="{% url 'produtos:lista' %}" class="btn btn-outline">← Cancelar</a>
                <h1>{% if edicao %}Editar{% else %}Novo{% endif %} Produto</h1>
            </div>
        </header>

        <div class="container">
            <div class="form-card">
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    
                    <!-- Mensagens -->
                    {% if messages %}
                        {% for message in messages %}
                        <div class="alert alert-{{ message.tags }}">
                            {{ message }}
                        </div>
                        {% endfor %}
                    {% endif %}

                    <div class="form-group">
                        <label for="nome">Nome do Produto *</label>
                        <input type="text" id="nome" name="nome" 
                               value="{% if produto %}{{ produto.nome }}{% endif %}"
                               required>
                    </div>

                    <div class="form-row">
                        <div class="form-group">
                            <label for="preco">Preço (R$) *</label>
                            <input type="number" id="preco" name="preco" 
                                   value="{% if produto %}{{ produto.preco }}{% endif %}"
                                   step="0.01" min="0" required>
                        </div>

                        <div class="form-group">
                            <label for="estoque">Estoque *</label>
                            <input type="number" id="estoque" name="estoque" 
                                   value="{% if produto %}{{ produto.estoque }}{% endif %}"
                                   min="0" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="categoria">Categoria *</label>
                        <select id="categoria" name="categoria" required>
                            <option value="">Selecione...</option>
                            {% for categoria in categorias %}
                            <option value="{{ categoria.id }}"
                                {% if produto and produto.categoria_id == categoria.id %}selected{% endif %}>
                                {{ categoria.nome }}
                            </option>
                            {% endfor %}
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="descricao">Descrição</label>
                        <textarea id="descricao" name="descricao" rows="4">{% if produto %}{{ produto.descricao }}{% endif %}</textarea>
                    </div>

                    <div class="form-group">
                        <label for="imagem">Imagem do Produto</label>
                        <input type="file" id="imagem" name="imagem" accept="image/*">
                        {% if produto.imagem %}
                        <p class="help-text">Imagem atual: {{ produto.imagem }}</p>
                        {% endif %}
                    </div>

                    <div class="form-actions">
                        <button type="submit" class="btn btn-primary">
                            {% if edicao %}Salvar Alterações{% else %}Cadastrar Produto{% endif %}
                        </button>
                        <a href="{% url 'produtos:lista' %}" class="btn btn-outline">Cancelar</a>
                    </div>
                </form>
            </div>
        </div>
    </main>

    <script src="{% static 'js/style.js' %}"></script>
</body>
</html>
```

---

## 💅 CSS do Projeto

**static/css/style.css** (principais estilos):
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

