# Guia de Referência Rápida - Django Básico

> **💡 Nota Importante:** Este guia contém comandos e conceitos de várias unidades do curso. 
> - **Unidade 1:** Ambiente virtual, instalação Django, criação de projeto
> - **Unidade 2:** Criação de apps, URLs, Views
> - **Unidade 3:** Models, Migrations, Forms

---

## 🚀 Comandos Essenciais

### Gerenciamento de Projeto

```bash
# Criar projeto
django-admin startproject nome_projeto
django-admin startproject nome_projeto .  # Na pasta atual

# Criar app (Unidade 2)
python manage.py startapp nome_app

# Servidor de desenvolvimento
python manage.py runserver
python manage.py runserver 8080  # Porta específica

# Shell interativo
python manage.py shell
```

### Banco de Dados

```bash
# Criar migrations
python manage.py makemigrations
python manage.py makemigrations nome_app  # App específico

# Aplicar migrations
python manage.py migrate

# Ver SQL da migration
python manage.py sqlmigrate app_name 0001

# Reverter migration
python manage.py migrate app_name 0001
```

### Usuários e Admin

```bash
# Criar superusuário
python manage.py createsuperuser

# Mudar senha de usuário
python manage.py changepassword username
```

---

## 📁 Estrutura de Diretórios

> **📚 Unidade 2:** A estrutura completa com apps é apresentada na Unidade 2.

```
meu_projeto/
├── venv/                       # Ambiente virtual
├── meu_projeto/               # Configurações
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app_nome/                  # Aplicação (Unidade 2)
│   ├── migrations/
│   ├── templates/
│   │   └── app_nome/
│   ├── static/
│   │   └── app_nome/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/                    # Estáticos globais
├── media/                     # Uploads
├── templates/                 # Templates globais
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Settings.py - Configurações Principais

```python
# Segurança
SECRET_KEY = 'sua-chave-secreta'
DEBUG = True  # False em produção
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'seu_app',  # Adicione aqui (Unidade 2)
]

# Database (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# Arquivos Estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 🔗 URLs - Roteamento

> **📚 Unidade 2:** URLs, roteamento e views são apresentados na Unidade 2.

### urls.py do Projeto

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### urls.py do App

```python
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detalhe, name='detalhe'),
    path('<slug:slug>/', views.por_slug, name='slug'),
    path('criar/', views.criar, name='criar'),
    path('<int:id>/editar/', views.editar, name='editar'),
    path('<int:id>/deletar/', views.deletar, name='deletar'),
]
```

---

## 👁️ Views - Function-Based

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Modelo

# View simples
def index(request):
    return HttpResponse("Olá!")

# Com template
def lista(request):
    itens = Modelo.objects.all()
    return render(request, 'app/lista.html', {'itens': itens})

# Com parâmetro
def detalhe(request, id):
    item = get_object_or_404(Modelo, id=id)
    return render(request, 'app/detalhe.html', {'item': item})

# GET e POST
def criar(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        # ... processar ...
        return redirect('app:lista')
    return render(request, 'app/form.html')

# JSON Response
def api(request):
    data = {'mensagem': 'Olá', 'status': 'ok'}
    return JsonResponse(data)
```

---

## 📄 Templates - Django Template Language

### Estrutura Básica

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>{% block title %}Título{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    {% block content %}
    <!-- Conteúdo aqui -->
    {% endblock %}
    
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

### Variáveis e Filtros

```html
<!-- Variáveis -->
{{ variavel }}
{{ objeto.atributo }}
{{ dicionario.chave }}
{{ lista.0 }}

<!-- Filtros -->
{{ texto|lower }}
{{ texto|upper }}
{{ texto|title }}
{{ texto|truncatewords:10 }}
{{ data|date:"d/m/Y" }}
{{ numero|floatformat:2 }}
{{ texto|default:"Valor padrão" }}
```

### Tags

```html
<!-- If -->
{% if condicao %}
    <!-- código -->
{% elif outra_condicao %}
    <!-- código -->
{% else %}
    <!-- código -->
{% endif %}

<!-- For -->
{% for item in lista %}
    {{ item.nome }}
    {% empty %}
    <p>Lista vazia</p>
{% endfor %}

<!-- URL -->
<a href="{% url 'app:detalhe' id=item.id %}">Link</a>
<a href="{% url 'app:slug' slug=item.slug %}">Link</a>

<!-- CSRF Token -->
<form method="post">
    {% csrf_token %}
    <!-- campos -->
</form>

<!-- Include -->
{% include 'partials/navbar.html' %}

<!-- Extends -->
{% extends 'base.html' %}
```

---

## 🗄️ Models - Banco de Dados

```python
from django.db import models

class Artigo(models.Model):
    # Campos
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    conteudo = models.TextField()
    publicado = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    # Relações
    autor = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    
    # Meta
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
    
    # Métodos
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('blog:detalhe', kwargs={'slug': self.slug})
```

### Tipos de Campos

```python
# Textos
CharField(max_length=100)
TextField()
SlugField()
EmailField()
URLField()

# Números
IntegerField()
DecimalField(max_digits=10, decimal_places=2)
FloatField()

# Data/Hora
DateField()
TimeField()
DateTimeField()
DateTimeField(auto_now_add=True)  # Criação
DateTimeField(auto_now=True)      # Atualização

# Booleano
BooleanField()

# Arquivos
FileField(upload_to='documentos/')
ImageField(upload_to='imagens/')

# Relações
ForeignKey('OutroModel', on_delete=models.CASCADE)
OneToOneField('OutroModel', on_delete=models.CASCADE)
ManyToManyField('OutroModel')
```

---

## 🔍 QuerySets - Consultas

```python
# Todos os registros
Model.objects.all()

# Filtrar
Model.objects.filter(campo=valor)
Model.objects.filter(campo__icontains='texto')
Model.objects.filter(numero__gt=10)  # maior que
Model.objects.filter(numero__lt=10)  # menor que
Model.objects.filter(numero__gte=10)  # maior ou igual
Model.objects.exclude(campo=valor)

# Obter um único
Model.objects.get(id=1)
Model.objects.first()
Model.objects.last()

# Ordenar
Model.objects.order_by('campo')
Model.objects.order_by('-campo')  # decrescente

# Limitar
Model.objects.all()[:10]

# Contar
Model.objects.count()

# Existe?
Model.objects.filter(campo=valor).exists()

# Criar
obj = Model.objects.create(campo1=valor1, campo2=valor2)

# Atualizar
obj.campo = novo_valor
obj.save()

# Deletar
obj.delete()
```

---

## 📋 Cheat Sheet de Atalhos

| Tarefa | Código |
|--------|--------|
| Ativar venv | `source venv/bin/activate` |
| Desativar venv | `deactivate` |
| Instalar Django | `pip install django` |
| Salvar deps | `pip freeze > requirements.txt` |
| Instalar deps | `pip install -r requirements.txt` |
| Criar projeto | `django-admin startproject nome .` |
| Criar app | `python manage.py startapp nome` |
| Rodar servidor | `python manage.py runserver` |
| Fazer migrations | `python manage.py makemigrations` |
| Aplicar migrations | `python manage.py migrate` |
| Criar superuser | `python manage.py createsuperuser` |
| Shell | `python manage.py shell` |

---

## 🎯 Padrão MVT Resumido

```
REQUEST → URLs → VIEW → MODEL (DB)
                  ↓
              TEMPLATE
                  ↓
              RESPONSE
```

---

## 📦 .gitignore Básico

```gitignore
# Python
__pycache__/
*.py[cod]
*.so
.Python

# Django
*.log
db.sqlite3
media/

# Venv
venv/
env/

# IDE
.vscode/
.idea/

# OS
.DS_Store

# Env
.env
```

---

## 🔐 Segurança - Checklist Produção

- [ ] `DEBUG = False`
- [ ] `SECRET_KEY` em variável de ambiente
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use HTTPS
- [ ] Configure banco de dados de produção
- [ ] Configure arquivos estáticos (`collectstatic`)
- [ ] Configure email backend
- [ ] Implemente backup de banco de dados

---

Esta referência cobre os conceitos básicos da Semana 1-2. Mantenha à mão!
