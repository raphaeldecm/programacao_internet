# Configuração e Estrutura Django - Parte 2

## Settings e Configurações Essenciais

## 🎯 Objetivos de Aprendizagem

- Compreender o arquivo `settings.py`
- Configurar banco de dados
- Gerenciar arquivos estáticos
- Configurar timezone e idioma
- Entender variáveis de ambiente e segurança

---

## 1. O arquivo settings.py

O `settings.py` é o coração das configurações do Django. Vamos explorar as principais seções:

### Estrutura Básica

```python
"""
Django settings for meu_projeto project.
"""

from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent
```

**BASE_DIR**: Caminho absoluto do diretório raiz do projeto. Útil para referenciar outros arquivos.

---

## 2. Segurança

### SECRET_KEY

```python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sua-chave-aqui'
```

**⚠️ IMPORTANTE:**
- Usada para criptografia e assinaturas
- **NUNCA** exponha em repositórios públicos
- Mude em produção
- Use variáveis de ambiente

### DEBUG

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
```

**DEBUG = True**
- ✅ Desenvolvimento: mostra erros detalhados
- ❌ Produção: expõe informações sensíveis

**DEBUG = False**
- ✅ Produção: mensagens genéricas de erro
- Requer configuração de `ALLOWED_HOSTS`

### ALLOWED_HOSTS

```python
ALLOWED_HOSTS = []  # Desenvolvimento

# Produção
ALLOWED_HOSTS = [
    'meusite.com',
    'www.meusite.com',
    '192.168.1.100',
]
```

Define quais domínios podem servir a aplicação.

---

## 3. Aplicações Instaladas

### INSTALLED_APPS

```python
INSTALLED_APPS = [
    # Apps padrão do Django
    'django.contrib.admin',        # Interface administrativa
    'django.contrib.auth',         # Sistema de autenticação
    'django.contrib.contenttypes', # Framework de tipos de conteúdo
    'django.contrib.sessions',     # Framework de sessões
    'django.contrib.messages',     # Framework de mensagens
    'django.contrib.staticfiles',  # Gerenciamento de arquivos estáticos
    
    # Apps de terceiros
    'rest_framework',              # Django REST Framework
    'corsheaders',                 # CORS headers
    
    # Seus apps
    'blog.apps.BlogConfig',        # Forma completa
    'usuarios',                    # Forma simplificada
    'portfolio',
]
```

**Ordem importa!** Apps listados primeiro têm prioridade em:
- Templates
- Arquivos estáticos
- Comandos do manage.py

---

## 4. Middleware

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

**Middleware**: Componentes que processam requisições/respostas globalmente.

**Ordem importa!** A requisição passa pelos middlewares de cima para baixo, e a resposta de baixo para cima.

---

## 5. Configuração de URLs

```python
ROOT_URLCONF = 'meu_projeto.urls'
```

Aponta para o arquivo principal de roteamento de URLs.

---

## 6. Templates

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

### Estrutura de Templates

```
meu_projeto/
├── templates/              # Templates globais
│   ├── base.html
│   └── navbar.html
└── blog/
    └── templates/
        └── blog/          # Templates do app blog
            ├── lista.html
            └── detalhe.html
```

---

## 7. Configuração de Banco de Dados

### SQLite (Padrão - Desenvolvimento)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### PostgreSQL (Recomendado para Produção)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Instale o driver:
```bash
pip install psycopg2-binary
```

### MySQL

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Instale o driver:
```bash
pip install mysqlclient
```

---

## 8. Validação de Senhas

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```

Define regras para senhas de usuários:
- Não pode ser similar ao username
- Mínimo de 8 caracteres
- Não pode ser senha comum
- Não pode ser apenas números

---

## 9. Internacionalização e Localização

### Idioma

```python
LANGUAGE_CODE = 'pt-br'  # Português do Brasil
# LANGUAGE_CODE = 'en-us'  # Inglês
# LANGUAGE_CODE = 'es'     # Espanhol
```

### Timezone

```python
TIME_ZONE = 'America/Sao_Paulo'  # Brasília
# TIME_ZONE = 'UTC'                # Padrão
# TIME_ZONE = 'America/New_York'   # Nova York
```

### Habilitar i18n e l10n

```python
USE_I18N = True   # Internacionalização
USE_L10N = True   # Localização
USE_TZ = True     # Timezone aware datetimes
```

---

## 10. Arquivos Estáticos (CSS, JS, Imagens)

### Configuração em Desenvolvimento

```python
# URL para acessar arquivos estáticos
STATIC_URL = '/static/'

# Diretórios adicionais de arquivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Diretório onde collectstatic vai reunir os arquivos (produção)
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### Estrutura de Arquivos Estáticos

```
meu_projeto/
├── static/                  # Arquivos estáticos globais
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── img/
│       └── logo.png
└── blog/
    └── static/
        └── blog/           # Namespace do app
            ├── css/
            └── js/
```

### Usando nos Templates

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <img src="{% static 'img/logo.png' %}" alt="Logo">
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

---

## 11. Arquivos de Upload (Media)

```python
# URL para acessar arquivos de upload
MEDIA_URL = '/media/'

# Diretório onde arquivos de upload serão salvos
MEDIA_ROOT = BASE_DIR / 'media'
```

### Configurar URLs para Media (urls.py)

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # suas urls aqui
]

# Apenas em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 12. Variáveis de Ambiente

### Por que usar?

- 🔒 Segurança: não expor senhas no código
- 🌍 Flexibilidade: diferentes configs em dev/prod
- 👥 Colaboração: cada dev tem suas próprias configs

### Usando python-decouple

```bash
pip install python-decouple
```

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=localhost,127.0.0.1
```

**settings.py:**

```python
from decouple import config, Csv

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Database
DATABASE_URL = config('DATABASE_URL')
```

**⚠️ Adicione .env ao .gitignore!**

---

## 13. Configurações para Produção

### settings.py dividido

Estrutura recomendada:

```
meu_projeto/
└── settings/
    ├── __init__.py
    ├── base.py        # Configurações comuns
    ├── development.py # Desenvolvimento
    └── production.py  # Produção
```

**base.py**: Configurações comuns
```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    # apps comuns
]
# configurações comuns
```

**development.py**:
```python
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**production.py**:
```python
from .base import *
from decouple import config

DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    # PostgreSQL config
}
```

**Usar:**
```bash
# Desenvolvimento
python manage.py runserver --settings=meu_projeto.settings.development

# Produção
export DJANGO_SETTINGS_MODULE=meu_projeto.settings.production
```

---

## 14. Outras Configurações Úteis

### Default Auto Field

```python
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

Define o tipo padrão para campos de chave primária.

### Login URLs

```python
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

### Email

```python
# Desenvolvimento (console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Produção (SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
```

---

## 📝 Exercício Prático

### Configure seu projeto:

1. Configure `LANGUAGE_CODE` para português
2. Ajuste `TIME_ZONE` para São Paulo
3. Crie pasta `static/` e `templates/` na raiz
4. Configure `STATICFILES_DIRS` e `MEDIA_ROOT`
5. Instale python-decouple
6. Crie arquivo `.env` com SECRET_KEY e DEBUG
7. Modifique settings.py para usar variáveis de ambiente
8. Adicione `.env` ao `.gitignore`

---

## 🔗 Recursos Adicionais

- [Django Settings](https://docs.djangoproject.com/en/5.0/ref/settings/)
- [Managing Static Files](https://docs.djangoproject.com/en/5.0/howto/static-files/)
- [Python Decouple](https://github.com/HBNetwork/python-decouple)

---

**Próxima Aula:** Sistema de URLs e Roteamento
