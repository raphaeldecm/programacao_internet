# Configuração e Estrutura Django - Parte 4

## Views e Protocolo HTTP

## 🎯 Objetivos de Aprendizagem

- Compreender o papel das Views no Django
- Criar Function-Based Views (FBV)
- Entender requisições e respostas HTTP
- Trabalhar com métodos GET e POST
- Implementar CSRF Protection
- Retornar diferentes tipos de respostas

---

## 1. O que são Views?

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

## 2. Criando Views Básicas

### View Simples

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

Acesse: `http://127.0.0.1:8000/hello/`

### View com HTML

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

### View com Template (Recomendado)

```python
from django.shortcuts import render

def home(request):
    context = {
        'titulo': 'Minha Página',
        'mensagem': 'Bem-vindo ao Django!',
    }
    return render(request, 'home.html', context)
```

---

## 3. O Objeto Request

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
    
    # Cabeçalhos HTTP
    user_agent = request.META.get('HTTP_USER_AGENT')
    ip_address = request.META.get('REMOTE_ADDR')
    
    # Arquivos enviados
    arquivo = request.FILES.get('arquivo')
    
    # Caminho da URL
    caminho = request.path  # '/blog/5/'
    caminho_completo = request.get_full_path()  # '/blog/5/?page=2'
    
    # Cookies
    session_id = request.COOKIES.get('sessionid')
    
    return HttpResponse("Informações processadas!")
```

---

## 4. Métodos HTTP: GET vs POST

### GET - Obter Dados

```python
def buscar_produtos(request):
    # URL: /produtos/?categoria=eletronicos&preco_max=1000
    
    categoria = request.GET.get('categoria', 'todos')
    preco_max = request.GET.get('preco_max')
    
    # Buscar produtos no banco
    produtos = Produto.objects.filter(categoria=categoria)
    
    if preco_max:
        produtos = produtos.filter(preco__lte=preco_max)
    
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

### POST - Enviar/Modificar Dados

```python
def criar_produto(request):
    if request.method == 'POST':
        # Processar formulário
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        
        # Criar produto
        produto = Produto.objects.create(
            nome=nome,
            preco=preco,
            descricao=descricao
        )
        
        # Redirecionar após sucesso
        return redirect('produto_detalhe', produto_id=produto.id)
    
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

## 5. CSRF Protection

### O que é CSRF?

**Cross-Site Request Forgery**: Ataque onde um site malicioso engana o usuário a executar ações indesejadas em um site onde ele está autenticado.

### Como o Django Protege

```python
# View
def criar_post(request):
    if request.method == 'POST':
        # Django valida o token automaticamente
        titulo = request.POST.get('titulo')
        # ... processar
```

```html
<!-- Template -->
<form method="post">
    {% csrf_token %}  <!-- TOKEN OBRIGATÓRIO! -->
    <input type="text" name="titulo">
    <button type="submit">Enviar</button>
</form>
```

### O que o {% csrf_token %} gera:

```html
<input type="hidden" name="csrfmiddlewaretoken" value="...token_unico...">
```

### Sem CSRF Token = Erro 403

```
Forbidden (403)
CSRF verification failed. Request aborted.
```

### Desabilitar CSRF (Não Recomendado!)

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def minha_api_view(request):
    # View sem proteção CSRF
    pass
```

---

## 6. Tipos de Respostas

### HttpResponse

```python
from django.http import HttpResponse

def texto_simples(request):
    return HttpResponse("Texto simples")

def html_direto(request):
    html = "<h1>Título</h1><p>Parágrafo</p>"
    return HttpResponse(html)

def com_status(request):
    return HttpResponse("Não encontrado", status=404)
```

### JsonResponse

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

def api_erro(request):
    return JsonResponse(
        {'erro': 'Produto não encontrado'},
        status=404
    )
```

### Render (Template)

```python
from django.shortcuts import render

def pagina(request):
    context = {
        'titulo': 'Minha Página',
        'itens': ['Item 1', 'Item 2', 'Item 3'],
    }
    return render(request, 'pagina.html', context)
```

### Redirect

```python
from django.shortcuts import redirect

def redirecionar_home(request):
    return redirect('/')

def redirecionar_nomeado(request):
    return redirect('blog:lista')

def redirecionar_com_params(request):
    return redirect('blog:detalhe', post_id=5)
```

### FileResponse

```python
from django.http import FileResponse
import os

def download_pdf(request):
    arquivo = open('documento.pdf', 'rb')
    response = FileResponse(arquivo)
    response['Content-Disposition'] = 'attachment; filename="documento.pdf"'
    return response
```

### HttpResponseNotFound (404)

```python
from django.http import HttpResponseNotFound

def pagina_nao_existe(request):
    return HttpResponseNotFound("<h1>Página não encontrada</h1>")
```

---

## 7. Shortcuts Úteis

### get_object_or_404

```python
from django.shortcuts import get_object_or_404
from .models import Produto

def detalhe_produto(request, produto_id):
    # Se não encontrar, retorna 404 automaticamente
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produto.html', {'produto': produto})

# Equivalente a:
def detalhe_produto_manual(request, produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
    except Produto.DoesNotExist:
        return HttpResponseNotFound("Produto não encontrado")
    return render(request, 'produto.html', {'produto': produto})
```

### get_list_or_404

```python
from django.shortcuts import get_list_or_404

def produtos_categoria(request, categoria_slug):
    # Se a lista estiver vazia, retorna 404
    produtos = get_list_or_404(Produto, categoria__slug=categoria_slug)
    return render(request, 'produtos.html', {'produtos': produtos})
```

---

## 8. Exemplo Completo: CRUD

```python
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Produto

# CREATE
def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        
        produto = Produto.objects.create(
            nome=nome,
            preco=preco,
            descricao=descricao
        )
        
        return redirect('produto_detalhe', produto_id=produto.id)
    
    return render(request, 'produtos/form.html')

# READ (Lista)
def listar_produtos(request):
    produtos = Produto.objects.all()
    
    # Filtro por busca
    busca = request.GET.get('q')
    if busca:
        produtos = produtos.filter(nome__icontains=busca)
    
    context = {'produtos': produtos}
    return render(request, 'produtos/lista.html', context)

# READ (Detalhe)
def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    context = {'produto': produto}
    return render(request, 'produtos/detalhe.html', context)

# UPDATE
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.preco = request.POST.get('preco')
        produto.descricao = request.POST.get('descricao')
        produto.save()
        
        return redirect('produto_detalhe', produto_id=produto.id)
    
    context = {'produto': produto}
    return render(request, 'produtos/form.html', context)

# DELETE
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    
    context = {'produto': produto}
    return render(request, 'produtos/confirmar_delete.html', context)
```

---

## 9. Decorators Úteis

### require_http_methods

```python
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def minha_view(request):
    # Só aceita GET e POST
    pass

# Atalhos
from django.views.decorators.http import require_GET, require_POST

@require_GET
def apenas_get(request):
    pass

@require_POST
def apenas_post(request):
    pass
```

### login_required

```python
from django.contrib.auth.decorators import login_required

@login_required
def area_restrita(request):
    # Usuário precisa estar logado
    return render(request, 'restrita.html')

@login_required(login_url='/entrar/')
def personalizado(request):
    # Redireciona para /entrar/ se não logado
    pass
```

---

## 10. Boas Práticas

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

# Use get_object_or_404()
produto = get_object_or_404(Produto, id=produto_id)

# Valide método HTTP
def minha_view(request):
    if request.method == 'POST':
        # processar
        pass
    return render(request, 'template.html')
```

### ❌ Evite

```python
# Não use try/except para 404
try:
    produto = Produto.objects.get(id=5)
except Produto.DoesNotExist:
    return HttpResponse("Não encontrado")
# Use: get_object_or_404()

# Não processe POST sem verificar método
def criar(request):
    # RUIM: sempre processa como POST
    nome = request.POST.get('nome')
    
# Não esqueça redirect após POST  
def criar(request):
    if request.method == 'POST':
        # criar...
        return render(request, 'form.html')  # RUIM!
        # Use: return redirect()
```

---

## 📝 Exercício Prático

### Crie um sistema de tarefas (To-Do):

1. **View de listagem** (`/tarefas/`)
   - Mostrar todas as tarefas
   - Filtrar por status (pendente/concluída)

2. **View de criação** (`/tarefas/nova/`)
   - Formulário para criar tarefa
   - Redirecionar para lista após criar

3. **View de detalhe** (`/tarefas/5/`)
   - Mostrar detalhes da tarefa

4. **View de edição** (`/tarefas/5/editar/`)
   - Formulário preenchido
   - Atualizar tarefa

5. **View de deleção** (`/tarefas/5/deletar/`)
   - Confirmar deleção
   - Deletar e redirecionar

**Requisitos:**
- Use `get_object_or_404()`
- Implemente CSRF protection
- Redirecione após POST
- Valide métodos HTTP

---

## 🔗 Recursos Adicionais

- [View Functions](https://docs.djangoproject.com/en/5.0/topics/http/views/)
- [Request/Response Objects](https://docs.djangoproject.com/en/5.0/ref/request-response/)
- [Shortcuts](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/)

---

**Próxima Aula:** Templates e Django Template Language
