# Aula 02 - URLs e Views

## 🎯 Objetivos de Aprendizagem

Ao final desta aula, você será capaz de:
- Criar e organizar apps Django
- Compreender o sistema de roteamento de URLs
- Criar Function-Based Views (FBV)
- Trabalhar com parâmetros em URLs
- Entender requisições e respostas HTTP
- Trabalhar com métodos GET e POST
- Implementar CSRF Protection

---

## 1. Criando Apps Django

### 1.1. O que são Apps?

No Django, um **projeto** é uma coleção de configurações e **apps**. Um **app** é um módulo web que faz algo específico (blog, loja, fórum, etc.).

**Diferenças:**
- **Projeto:** configuração geral (settings, URLs principais)
- **App:** funcionalidade específica com seus próprios models, views, templates

**Vantagens:**
- ✅ Organização modular
- ✅ Reutilização em outros projetos
- ✅ Separação de responsabilidades
- ✅ Manutenção facilitada

### 1.2. Criando um App

```bash
# Comando para criar app
python manage.py startapp blog
```

Este comando cria a seguinte estrutura:

```
blog/
├── __init__.py          # Torna o diretório um pacote Python
├── admin.py            # Configurações do Django Admin
├── apps.py             # Configurações do app
├── migrations/         # Histórico de mudanças no banco
│   └── __init__.py
├── models.py           # Modelos (estrutura de dados)
├── tests.py            # Testes automatizados
└── views.py            # Lógica de visualização
```

### 1.3. Registrando o App

Abra `settings.py` e adicione o app em `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # ⬅️ Seu app
]
```

> **Por que registrar?** O Django precisa saber quais apps fazem parte do projeto para carregar seus templates, static files, migrations, etc.

---

## 2. Sistema de URLs e Roteamento

### 2.1. Como funciona o Roteamento

```
┌─────────────────────────────────────────┐
│  Requisição: http://site.com/blog/5/   │
└──────────────────┬──────────────────────┘
                   │
                   ▼
          ┌────────────────────┐
          │  urls.py (projeto) │
          │  ROOT_URLCONF      │
          └─────────┬──────────┘
                    │
                    ▼
          ┌────────────────────┐
          │  urls.py (app)     │
          │  include()         │
          └─────────┬──────────┘
                    │
                    ▼
          ┌────────────────────┐
          │  View Function     │
          │  ou Class-Based    │
          └─────────┬──────────┘
                    │
                    ▼
          ┌──────────────────────┐
          │  HttpResponse        │
          │  (HTML, JSON, etc)   │
          └──────────────────────┘
```

### 2.2. URLs no Projeto Principal

**meu_projeto/urls.py:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Apps
    path('', include('home.urls')),           # Página inicial
    path('blog/', include('blog.urls')),      # Blog
    path('contato/', include('contato.urls')),# Contato
]
```

### 2.3. URLs dentro de Apps

Crie o arquivo **blog/urls.py**:

```python
from django.urls import path
from . import views

app_name = 'blog'  # Namespace do app

urlpatterns = [
    # /blog/
    path('', views.lista_posts, name='lista'),
    
    # /blog/5/
    path('<int:post_id>/', views.detalhe_post, name='detalhe'),
    
    # /blog/novo/
    path('novo/', views.criar_post, name='criar'),
    
    # /blog/5/editar/
    path('<int:post_id>/editar/', views.editar_post, name='editar'),
    
    # /blog/5/deletar/
    path('<int:post_id>/deletar/', views.deletar_post, name='deletar'),
    
    # /blog/categoria/tecnologia/
    path('categoria/<slug:slug>/', views.posts_por_categoria, name='categoria'),
]
```

---

## 3. Função path() e Converters

### 3.1. Sintaxe da Função path()

```python
path(route, view, kwargs=None, name=None)
```

**Parâmetros:**
1. **route**: String com o padrão da URL
2. **view**: Função ou classe de view
3. **kwargs**: Dicionário de argumentos extras (opcional)
4. **name**: Nome único para a URL (recomendado!)

### 3.2. Path Converters

| Converter | Descrição | Exemplo | Regex Equivalente |
|-----------|-----------|---------|-------------------|
| `str` | Qualquer string (exceto `/`) | `<str:nome>` | `[^/]+` |
| `int` | Inteiro positivo ou zero | `<int:id>` | `[0-9]+` |
| `slug` | Slug (letras, números, - e _) | `<slug:slug>` | `[-a-zA-Z0-9_]+` |
| `uuid` | UUID | `<uuid:id>` | UUID format |
| `path` | Qualquer string (inclui `/`) | `<path:caminho>` | `.+` |

### 3.3. Exemplos Práticos

```python
urlpatterns = [
    # str: captura qualquer texto
    path('perfil/<str:username>/', views.perfil),
    # Captura: /perfil/joao123/
    
    # int: apenas números
    path('produto/<int:produto_id>/', views.produto),
    # Captura: /produto/42/
    # Não captura: /produto/abc/
    
    # slug: formato de URL amigável
    path('artigo/<slug:slug>/', views.artigo),
    # Captura: /artigo/django-para-iniciantes/
    # Não captura: /artigo/Django para Iniciantes/
    
    # múltiplos parâmetros
    path('arquivo/<int:ano>/<int:mes>/', views.arquivo),
    # Captura: /arquivo/2024/02/
]
```

---

## 4. Nomeando URLs

### 4.1. Por que nomear URLs?

```python
# ❌ Ruim: URL hardcoded
<a href="/blog/5/">Ver Post</a>

# ✅ Bom: Usando nome da URL
<a href="{% url 'blog:detalhe' post_id=5 %}">Ver Post</a>
```

**Vantagens:**
- Fácil refatoração
- Menos erros
- Código mais limpo
- URLs dinâmicas

### 4.2. Usando Namespaces

```python
# blog/urls.py
app_name = 'blog'  # Define o namespace

urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:id>/', views.detalhe, name='detalhe'),
]
```

### 4.3. Usando em Templates

```html
<!-- URL simples -->
<a href="{% url 'blog:lista' %}">Ver todos os posts</a>
<!-- Gera: /blog/ -->

<!-- URL com parâmetro -->
<a href="{% url 'blog:detalhe' post_id=post.id %}">{{ post.titulo }}</a>
<!-- Gera: /blog/5/ -->

<!-- URL com múltiplos parâmetros -->
<a href="{% url 'blog:arquivo' ano=2024 mes=2 %}">Fevereiro 2024</a>
<!-- Gera: /blog/arquivo/2024/2/ -->
```

### 4.4. Usando em Views (Python)

```python
from django.shortcuts import redirect
from django.urls import reverse

def minha_view(request):
    # Método 1: redirect com nome
    return redirect('blog:lista')
    
    # Método 2: redirect com parâmetros
    return redirect('blog:detalhe', post_id=5)
    
    # Método 3: reverse (gera a URL)
    url = reverse('blog:detalhe', kwargs={'post_id': 5})
    # url = '/blog/5/'
    return redirect(url)
```

---

## 5. O que são Views?

**Views** são funções ou classes Python que:
- Recebem requisições HTTP (request)
- Processam lógica de negócio
- Retornam respostas HTTP (response)

```python
┌─────────────┐
│  REQUEST    │
│  (Browser)  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   URLS      │
└──────┬──────┘
       │
       ▼
┌─────────────┐   ┌──────────┐
│   VIEW      │──►│  MODEL   │
│  (lógica)   │◄──│  (dados) │
└──────┬──────┘   └──────────┘
       │
       ▼
┌─────────────┐
│  TEMPLATE   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  RESPONSE   │
│  (Browser)  │
└─────────────┘
```

---

## 6. Criando Views Básicas

### 6.1. View Simples (HttpResponse)

```python
# views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Olá, Mundo!")
```

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
]
```

### 6.2. View com HTML Direto

```python
from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Minha Página</title>
    </head>
    <body>
        <h1>Bem-vindo!</h1>
        <p>Esta é minha primeira view Django.</p>
    </body>
    </html>
    """
    return HttpResponse(html)
```

### 6.3. View com Template (Recomendado)

```python
from django.shortcuts import render

def home(request):
    context = {
        'titulo': 'Minha Página',
        'mensagem': 'Bem-vindo ao Django!',
    }
    return render(request, 'home.html', context)
```

### 6.4. View com Parâmetros da URL

```python
from django.shortcuts import render, get_object_or_404
from .models import Post

def detalhe_post(request, post_id):
    # post_id vem da URL <int:post_id>
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalhe.html', {'post': post})

def posts_por_categoria(request, slug):
    # slug vem da URL <slug:slug>
    categoria = get_object_or_404(Categoria, slug=slug)
    posts = Post.objects.filter(categoria=categoria)
    return render(request, 'blog/categoria.html', {
        'categoria': categoria,
        'posts': posts
    })
```

---

## 7. O Objeto Request

O objeto `request` contém informações sobre a requisição HTTP:

```python
def minha_view(request):
    # Método HTTP
    metodo = request.method  # 'GET', 'POST', 'PUT', 'DELETE'
    
    # Parâmetros GET (query string)
    # URL: /buscar/?q=django&page=2
    termo = request.GET.get('q')  # 'django'
    pagina = request.GET.get('page')  # '2'
    
    # Dados POST (formulários)
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    # Informações do usuário
    usuario = request.user
    esta_logado = request.user.is_authenticated
    
    # Caminho da URL
    caminho = request.path  # '/blog/5/'
    caminho_completo = request.get_full_path()  # '/blog/5/?page=2'
    
    return HttpResponse("Informações processadas!")
```

---

## 8. Métodos HTTP: GET vs POST

### 8.1. GET - Obter Dados

```python
def buscar_produtos(request):
    # URL: /produtos/?categoria=eletronicos&preco_max=1000
    
    categoria = request.GET.get('categoria', 'todos')
    preco_max = request.GET.get('preco_max')
    
    # Buscar produtos (simulação)
    produtos = []  # aqui viriam dados reais do banco
    
    if preco_max:
        # filtrar por preço
        pass
    
    context = {'produtos': produtos}
    return render(request, 'produtos/lista.html', context)
```

**Características do GET:**
- ✅ Leitura de dados
- ✅ Pode ser favoritado/compartilhado
- ✅ Armazenado no histórico
- ❌ Não deve modificar dados
- ❌ Limite de tamanho (URL)
- ❌ Dados visíveis na URL

### 8.2. POST - Enviar/Modificar Dados

```python
def criar_produto(request):
    if request.method == 'POST':
        # Processar formulário
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        
        # Criar produto (simulação - sem banco ainda)
        # produto = Produto.objects.create(...)
        
        # Redirecionar após sucesso
        return redirect('produto_lista')
    
    # GET: Mostrar formulário vazio
    return render(request, 'produtos/form.html')
```

**Características do POST:**
- ✅ Criação/modificação de dados
- ✅ Sem limite de tamanho
- ✅ Dados não visíveis na URL
- ✅ Não fica no histórico
- ❌ Não pode ser favoritado
- ❌ Navegador pergunta ao recarregar

---

## 9. CSRF Protection

### 9.1. O que é CSRF?

**Cross-Site Request Forgery**: Ataque onde um site malicioso engana o usuário a executar ações indesejadas em um site onde ele está autenticado.

### 9.2. Como o Django Protege

```python
# View
def criar_post(request):
    if request.method == 'POST':
        # Django valida o token automaticamente
        titulo = request.POST.get('titulo')
        # ... processar
        return redirect('blog:lista')
    return render(request, 'blog/form.html')
```

```html
<!-- Template -->
<form method="post">
    {% csrf_token %}  <!-- TOKEN OBRIGATÓRIO! -->
    <input type="text" name="titulo">
    <button type="submit">Enviar</button>
</form>
```

### 9.3. O que o {% csrf_token %} gera:

```html
<input type="hidden" name="csrfmiddlewaretoken" value="...token_unico...">
```

**Sem CSRF Token = Erro 403:**
```
Forbidden (403)
CSRF verification failed. Request aborted.
```

---

## 10. Tipos de Respostas

### 10.1. HttpResponse

```python
from django.http import HttpResponse

def texto_simples(request):
    return HttpResponse("Texto simples")

def com_status(request):
    return HttpResponse("Não encontrado", status=404)
```

### 10.2. JsonResponse

```python
from django.http import JsonResponse

def api_produtos(request):
    data = {
        'produtos': [
            {'id': 1, 'nome': 'Notebook', 'preco': 3000},
            {'id': 2, 'nome': 'Mouse', 'preco': 50},
        ],
        'total': 2
    }
    return JsonResponse(data)
```

### 10.3. Render (Template)

```python
from django.shortcuts import render

def pagina(request):
    context = {
        'titulo': 'Minha Página',
        'itens': ['Item 1', 'Item 2', 'Item 3'],
    }
    return render(request, 'pagina.html', context)
```

### 10.4. Redirect

```python
from django.shortcuts import redirect

def redirecionar_home(request):
    return redirect('/')

def redirecionar_nomeado(request):
    return redirect('blog:lista')

def redirecionar_com_params(request):
    return redirect('blog:detalhe', post_id=5)
```

---

## 11. Shortcuts Úteis

### get_object_or_404

```python
from django.shortcuts import get_object_or_404
from .models import Produto

def detalhe_produto(request, produto_id):
    # Se não encontrar, retorna 404 automaticamente
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produto.html', {'produto': produto})
```

**Equivalente a:**
```python
from django.http import HttpResponseNotFound

def detalhe_produto_manual(request, produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
    except Produto.DoesNotExist:
        return HttpResponseNotFound("Produto não encontrado")
    return render(request, 'produto.html', {'produto': produto})
```

---

## 12. Exemplo Completo: Sistema de Páginas

**urls.py:**
```python
from django.urls import path
from . import views

app_name = 'paginas'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('servicos/', views.servicos, name='servicos'),
    path('contato/', views.contato, name='contato'),
]
```

**views.py:**
```python
from django.shortcuts import render, redirect

def index(request):
    context = {
        'titulo': 'Página Inicial',
        'descricao': 'Bem-vindo ao nosso site!',
    }
    return render(request, 'paginas/index.html', context)

def sobre(request):
    context = {
        'titulo': 'Sobre Nós',
        'missao': 'Nossa missão é...',
        'valores': ['Integridade', 'Qualidade', 'Inovação'],
    }
    return render(request, 'paginas/sobre.html', context)

def servicos(request):
    servicos_lista = [
        {'titulo': 'Desenvolvimento Web', 'descricao': '...'},
        {'titulo': 'Consultoria', 'descricao': '...'},
        {'titulo': 'Suporte', 'descricao': '...'},
    ]
    context = {'servicos': servicos_lista}
    return render(request, 'paginas/servicos.html', context)

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        
        # Aqui você processaria o formulário
        # Por exemplo, enviar email ou salvar no banco
        
        # Redirecionar após sucesso
        return redirect('paginas:index')
    
    context = {
        'titulo': 'Fale Conosco',
        'email': 'contato@empresa.com',
    }
    return render(request, 'paginas/contato.html', context)
```

---

## 13. Boas Práticas

### ✅ Faça

```python
# Use render() para templates
def minha_view(request):
    return render(request, 'template.html', context)

# Use redirect() após POST
def criar(request):
    if request.method == 'POST':
        # ... criar objeto ...
        return redirect('lista')  # Evita re-submissão
    return render(request, 'form.html')

# Use namespaces em URLs
app_name = 'blog'

# Use nomes descritivos
path('produtos/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto')

# Valide método HTTP
def minha_view(request):
    if request.method == 'POST':
        # processar
        pass
    return render(request, 'template.html')
```

### ❌ Evite

```python
# Não esqueça redirect após POST  
def criar(request):
    if request.method == 'POST':
        # criar...
        return render(request, 'form.html')  # RUIM!
        # Use: return redirect()

# Não use URLs hardcoded
<a href="/blog/5/">Post</a>  # RUIM!
# Use: {% url 'blog:detalhe' post_id=5 %}

# Não processe POST sem verificar método
def criar(request):
    nome = request.POST.get('nome')  # RUIM! E se for GET?
```

---

## 📝 Exercícios Práticos

### Exercício 1: Sistema de Páginas

Crie um site com:
1. Página inicial (`/`)
2. Sobre (`/sobre/`)
3. Serviços (`/servicos/`)
4. Contato (`/contato/`)

Requisitos:
- Crie um app chamado `paginas`
- Use namespaces
- Nomeie todas as URLs
- Crie views e templates básicos

### Exercício 2: Blog Simples

Crie um blog com:
1. Lista de posts (`/blog/`)
2. Detalhe de post com ID (`/blog/5/`)
3. Posts por categoria com slug (`/blog/categoria/tecnologia/`)

Requisitos:
- URLs com path converters
- Views que recebem parâmetros
- Use get_object_or_404 (quando estudarmos models)

### Exercício 3: Formulário de Contato

Crie um formulário que:
1. Exibe formulário em GET
2. Processa dados em POST
3. Redireciona após envio
4. Usa CSRF protection

---

## 🔗 Recursos Adicionais

- [Django URL Dispatcher](https://docs.djangoproject.com/en/5.0/topics/http/urls/)
- [View Functions](https://docs.djangoproject.com/en/5.0/topics/http/views/)
- [Request/Response Objects](https://docs.djangoproject.com/en/5.0/ref/request-response/)
- [Shortcuts](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/)

---

## 📚 Próxima Aula

Na **Aula 03**, você aprenderá:
- Django Template Language
- Herança de templates
- Tags e filtros
- Arquivos estáticos (CSS, JS, imagens)

---

**Continue praticando e nos vemos na próxima aula!** 🚀
