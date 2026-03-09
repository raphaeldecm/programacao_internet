# Configuração e Estrutura Django - Parte 3

## Sistema de URLs e Roteamento

## 🎯 Objetivos de Aprendizagem

- Compreender o sistema de roteamento do Django
- Criar e organizar URLs
- Trabalhar com parâmetros em URLs
- Usar namespaces e nomes de URLs
- Implementar redirecionamentos

---

## 1. Como funciona o Roteamento no Django

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

---

## 2. URLs no Projeto Principal

### meu_projeto/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

### Adicionando URLs de Apps

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Apps
    path('', include('home.urls')),           # Página inicial
    path('blog/', include('blog.urls')),      # Blog
    path('produtos/', include('loja.urls')),  # Loja
    path('contato/', include('contato.urls')),# Contato
]

# Servir arquivos de media em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

---

## 3. URLs dentro de Apps

### Criar blog/urls.py

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

## 4. Função path()

### Sintaxe

```python
path(route, view, kwargs=None, name=None)
```

### Parâmetros

1. **route**: String com o padrão da URL
2. **view**: Função ou classe de view
3. **kwargs**: Dicionário de argumentos extras (opcional)
4. **name**: Nome único para a URL (opcional, mas recomendado)

### Exemplos

```python
from django.urls import path
from . import views

urlpatterns = [
    # URL simples
    path('sobre/', views.sobre, name='sobre'),
    
    # Com parâmetro inteiro
    path('usuario/<int:id>/', views.perfil_usuario, name='perfil'),
    
    # Com parâmetro string
    path('buscar/<str:termo>/', views.buscar, name='buscar'),
    
    # Com parâmetro slug
    path('post/<slug:slug>/', views.post_detalhe, name='post'),
    
    # Com múltiplos parâmetros
    path('arquivo/<int:ano>/<int:mes>/', views.arquivo, name='arquivo'),
]
```

---

## 5. Converter de Caminho (Path Converters)

### Tipos Disponíveis

| Converter | Descrição | Exemplo | Regex Equivalente |
|-----------|-----------|---------|-------------------|
| `str` | Qualquer string (exceto `/`) | `<str:nome>` | `[^/]+` |
| `int` | Inteiro positivo ou zero | `<int:id>` | `[0-9]+` |
| `slug` | Slug (letras, números, - e _) | `<slug:slug>` | `[-a-zA-Z0-9_]+` |
| `uuid` | UUID | `<uuid:id>` | UUID format |
| `path` | Qualquer string (inclui `/`) | `<path:caminho>` | `.+` |

### Exemplos Práticos

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
    
    # uuid: identificador único
    path('pedido/<uuid:pedido_id>/', views.pedido),
    # Captura: /pedido/550e8400-e29b-41d4-a716-446655440000/
    
    # path: captura caminho completo
    path('docs/<path:caminho>/', views.documentacao),
    # Captura: /docs/tutorial/parte1/introducao/
]
```

---

## 6. Views Correspondentes

### blog/views.py

```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Categoria

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista.html', {'posts': posts})

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

def criar_post(request):
    # Lógica para criar post
    return render(request, 'blog/form.html')

def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Lógica para editar
    return render(request, 'blog/form.html', {'post': post})

def deletar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:lista')
    return render(request, 'blog/confirmar_delete.html', {'post': post})
```

---

## 7. Nomeando URLs (name)

### Por que nomear URLs?

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

### Definindo nomes

```python
# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.lista_posts, name='lista'),
    path('<int:post_id>/', views.detalhe_post, name='detalhe'),
    path('novo/', views.criar_post, name='criar'),
]
```

### Usando em Templates

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

### Usando em Views (Python)

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

## 8. Namespaces

### App Namespace

```python
# blog/urls.py
app_name = 'blog'  # Define o namespace

urlpatterns = [
    path('', views.lista, name='lista'),
]
```

```html
<!-- Usar em templates -->
{% url 'blog:lista' %}
```

### Instance Namespace

```python
# projeto/urls.py
urlpatterns = [
    path('blog/', include('blog.urls')),
    path('noticias/', include('blog.urls', namespace='noticias')),
]
```

Permite usar o mesmo app em múltiplas URLs com namespaces diferentes.

---

## 9. Include e Organização

### Include Simples

```python
# projeto/urls.py
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
]
```

### Include com Lista de Patterns

```python
from django.urls import path, include
from blog import views

blog_patterns = [
    path('', views.lista, name='lista'),
    path('<int:id>/', views.detalhe, name='detalhe'),
]

urlpatterns = [
    path('blog/', include(blog_patterns)),
]
```

---

## 10. Expressões Regulares (re_path)

Para padrões mais complexos, use `re_path`:

```python
from django.urls import re_path
from . import views

urlpatterns = [
    # CEP: 00000-000
    re_path(r'^cep/(?P<cep>\d{5}-\d{3})/$', views.buscar_cep, name='cep'),
    
    # Data: YYYY-MM-DD
    re_path(
        r'^arquivo/(?P<ano>[0-9]{4})/(?P<mes>[0-9]{2})/$',
        views.arquivo,
        name='arquivo'
    ),
    
    # Arquivo com extensão
    re_path(
        r'^download/(?P<filename>[\w.]+\.(pdf|zip))/$',
        views.download,
        name='download'
    ),
]
```

---

## 11. Redirecionamentos

### RedirectView

```python
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    # Redirecionar para outra URL
    path('inicio/', RedirectView.as_view(url='/home/')),
    
    # Redirecionar para URL nomeada
    path('perfil/', RedirectView.as_view(pattern_name='usuario:perfil')),
    
    # Redirecionamento permanente (301)
    path('old-page/', RedirectView.as_view(
        url='/new-page/',
        permanent=True
    )),
]
```

### Em Views

```python
from django.shortcuts import redirect

def minha_view(request):
    # Redirecionar para URL
    return redirect('/home/')
    
    # Redirecionar para URL nomeada
    return redirect('blog:lista')
    
    # Redirecionar para URL nomeada com parâmetros
    return redirect('blog:detalhe', post_id=5)
```

---

## 12. Boas Práticas de URLs

### ✅ Faça

```python
# Use nomes descritivos
path('produtos/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto')

# Use namespaces
app_name = 'loja'

# URLs RESTful
path('produtos/', views.lista_produtos, name='lista')  # GET
path('produtos/novo/', views.criar_produto, name='criar')  # GET/POST
path('produtos/<int:id>/', views.detalhe_produto, name='detalhe')  # GET
path('produtos/<int:id>/editar/', views.editar_produto, name='editar')  # GET/POST
path('produtos/<int:id>/deletar/', views.deletar_produto, name='deletar')  # POST

# Use slugs para URLs amigáveis
path('blog/<slug:slug>/', views.post, name='post')
```

### ❌ Evite

```python
# URLs muito longas
path('meu/super/caminho/muito/longo/produto/<int:id>/', ...)

# Parâmetros ambíguos
path('<int:id>/<int:id2>/', ...)  # Use nomes descritivos!

# Sem nomes
path('produtos/', views.lista)  # Sempre USE name!

# Caracteres especiais
path('produtos?categoria=tech', ...)  # Use parâmetros adequados
```

---

## 13. Tratamento de Erros

### URLs personalizadas para erros

```python
# projeto/urls.py
handler404 = 'meu_app.views.erro_404'
handler500 = 'meu_app.views.erro_500'
handler403 = 'meu_app.views.erro_403'
handler400 = 'meu_app.views.erro_400'
```

### Views de Erro

```python
# meu_app/views.py
from django.shortcuts import render

def erro_404(request, exception):
    return render(request, '404.html', status=404)

def erro_500(request):
    return render(request, '500.html', status=500)
```

---

## 📝 Exercício Prático

### Crie um sistema de blog com as seguintes URLs:

1. **Lista de posts**: `/blog/`
2. **Detalhe do post**: `/blog/5/` ou `/blog/meu-post-slug/`
3. **Posts por categoria**: `/blog/categoria/tecnologia/`
4. **Posts por autor**: `/blog/autor/joao/`
5. **Arquivo por data**: `/blog/2024/02/`
6. **Buscar posts**: `/blog/buscar/?q=django`
7. **Criar post**: `/blog/novo/`
8. **Editar post**: `/blog/5/editar/`
9. **Deletar post**: `/blog/5/deletar/`

**Requisitos:**
- Use namespaces (`app_name = 'blog'`)
- Nomeie todas as URLs
- Use path converters apropriados
- Crie views básicas (podem retornar HttpResponse simples)
- Teste todas as URLs no navegador

---

## 🔗 Recursos Adicionais

- [Django URL Dispatcher](https://docs.djangoproject.com/en/5.0/topics/http/urls/)
- [URL Namespaces](https://docs.djangoproject.com/en/5.0/topics/http/urls/#url-namespaces)
- [Reverse URL](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/)

---

**Próxima Aula:** Views e HttpResponse
