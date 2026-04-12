# Aula 01 - Introdução ao Django

## Objetivos de Aprendizagem

Ao final desta aula, você será capaz de:
- Criar e ativar ambientes virtuais Python
- Instalar e configurar o Django
- Compreender a estrutura de um projeto Django
- Entender o conceito MVT (Model-View-Template)
- Configurar as principais definições no arquivo settings.py
- Criar superusuário e acessar o Django Admin

---

## 1. Ambientes Virtuais (venv)

### O que é um Ambiente Virtual?

Um ambiente virtual é um diretório isolado que contém uma instalação Python independente, permitindo que você:
- Mantenha dependências de diferentes projetos separadas
- Evite conflitos entre versões de pacotes
- Facilite o deployment e compartilhamento do projeto

### Criando um Ambiente Virtual

```bash
# No terminal, navegue até a pasta do seu projeto
cd ~/projetos/meu_projeto

# Crie o ambiente virtual (Linux/Mac)
python3 -m venv venv

# Ou no Windows
python -m venv venv
```

### Ativando o Ambiente Virtual

```bash
# Linux/Mac
source venv/bin/activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate.bat
```

💡 **Dica:** Quando o ambiente está ativado, você verá `(venv)` no início da linha do terminal.

### Desativando o Ambiente Virtual

```bash
deactivate
```

---

## 2. Instalação do Django

### Instalando o Django

Com o ambiente virtual ativado:

```bash
# Instalar a versão mais recente
pip install django

# Ou instalar uma versão específica
pip install django==5.0

# Verificar a instalação
python -m django --version
```

### Salvando Dependências

```bash
# Criar arquivo de requisitos
pip freeze > requirements.txt

# Instalar dependências de um projeto existente
pip install -r requirements.txt
```

**Exemplo de requirements.txt:**
```
Django==5.0.2
asgiref==3.7.2
sqlparse==0.4.4
```

---

## 3. Criando um Projeto Django

### Estrutura Inicial

```bash
# Criar um novo projeto
django-admin startproject meu_projeto

# Ou criar na pasta atual (note o ponto no final)
django-admin startproject meu_projeto .
```

### Estrutura de Pastas Criada

```
meu_projeto/
│
├── meu_projeto/          # Pasta principal do projeto
│   ├── __init__.py       # Marca a pasta como pacote Python
│   ├── asgi.py           # Configuração ASGI (servidor assíncrono)
│   ├── settings.py       # Configurações do projeto
│   ├── urls.py           # Roteamento de URLs principal
│   └── wsgi.py           # Configuração WSGI (servidor web)
│
└── manage.py             # Ferramenta de linha de comando
```

### O arquivo manage.py

É a interface de linha de comando para interagir com o Django:

```bash
# Iniciar servidor de desenvolvimento
python manage.py runserver

# Criar migrations
python manage.py makemigrations

# Aplicar migrations
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Abrir shell interativo
python manage.py shell
```

---

## 4. Servidor de Desenvolvimento

### Iniciando o Servidor

```bash
python manage.py runserver

# Especificar porta
python manage.py runserver 8080

# Especificar IP e porta
python manage.py runserver 0.0.0.0:8000
```

### Acessando o Projeto

Abra o navegador e acesse: `http://127.0.0.1:8000/`

Você verá a página inicial do Django! 🚀

**Características do servidor:**
- ✅ Reinicia automaticamente ao detectar mudanças no código
- ✅ Apenas para desenvolvimento (não use em produção!)
- ✅ Mostra erros detalhados no navegador

---

## 5. Entendendo o Padrão MVT

Django utiliza o padrão **MVT** (Model-View-Template):

```
┌─────────────────────────────────────────┐
│         Requisição do Cliente           │
│              (Browser)                  │
└──────────────────┬──────────────────────┘
                   │
                   ▼
          ┌────────────────┐
          │   URLS (urls.py)│
          │  Roteamento     │
          └────────┬────────┘
                   │
                   ▼
          ┌────────────────┐
          │  VIEW (views.py)│
          │    Lógica       │
          └────┬──────┬─────┘
               │      │
       ┌───────┘      └───────┐
       ▼                      ▼
┌──────────────┐      ┌──────────────┐
│MODEL         │      │TEMPLATE      │
│(models.py)   │◄────►│(.html)       │
│Banco de Dados│      │Interface     │
└──────────────┘      └──────┬───────┘
                             │
                             ▼
                  ┌──────────────────┐
                  │  Resposta HTML   │
                  │   (Browser)      │
                  └──────────────────┘
```

### Componentes:

1. **Model (M)** - `models.py`
   - Define a estrutura dos dados
   - Interage com o banco de dados
   - ORM do Django

2. **View (V)** - `views.py`
   - Contém a lógica de negócio
   - Processa requisições HTTP
   - Retorna respostas (HTML, JSON, etc.)

3. **Template (T)** - `templates/*.html`
   - Define a apresentação (interface)
   - HTML com sintaxe do Django
   - Recebe dados da View

---

## 6. O Arquivo settings.py

O `settings.py` é o coração das configurações do Django. Vamos explorar as principais seções:

### 6.1. Estrutura Básica e Paths

```python
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent
```

**BASE_DIR**: Caminho absoluto do diretório raiz do projeto. Útil para referenciar outros arquivos.

---

### 6.2. Segurança

#### SECRET_KEY

```python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sua-chave-aqui'
```

**⚠️ IMPORTANTE:**
- Usada para criptografia e assinaturas
- **NUNCA** exponha em repositórios públicos
- Mude em produção
- Use variáveis de ambiente

#### DEBUG

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

#### ALLOWED_HOSTS

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

### 6.3. Aplicações Instaladas

```python
INSTALLED_APPS = [
    # Apps padrão do Django
    'django.contrib.admin',        # Interface administrativa
    'django.contrib.auth',         # Sistema de autenticação
    'django.contrib.contenttypes', # Framework de tipos de conteúdo
    'django.contrib.sessions',     # Framework de sessões
    'django.contrib.messages',     # Framework de mensagens
    'django.contrib.staticfiles',  # Gerenciamento de arquivos estáticos
    
    # Apps de terceiros (instalar depois)
    # 'rest_framework',
    
    # Seus apps (criar nas próximas aulas)
    # 'blog',
    # 'portfolio',
]
```

**Ordem importa!** Apps listados primeiro têm prioridade.

---

### 6.4. Configuração de Banco de Dados

#### SQLite (Padrão - Desenvolvimento)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

SQLite é perfeito para desenvolvimento e projetos pequenos. Não requer instalação separada.

#### PostgreSQL (Recomendado para Produção)

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

Instale o driver: `pip install psycopg2-binary`

---

### 6.5. Internacionalização e Localização

```python
# Idioma
LANGUAGE_CODE = 'pt-br'  # Português do Brasil

# Timezone
TIME_ZONE = 'America/Fortaleza'  # ou seu fuso horário

# Habilitar i18n e l10n
USE_I18N = True   # Internacionalização
USE_L10N = True   # Localização
USE_TZ = True     # Timezone aware datetimes
```

Configurar corretamente garante que datas, horas e textos apareçam no formato brasileiro.

---

### 6.6. Arquivos Estáticos (CSS, JS, Imagens)

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

---

### 6.7. Arquivos de Upload (Media)

```python
# URL para acessar arquivos de upload
MEDIA_URL = '/media/'

# Diretório onde arquivos de upload serão salvos
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 7. Migrações Iniciais e Django Admin

### 7.1. Executar Migrações

As migrações criam as tabelas necessárias no banco de dados:

```bash
python manage.py migrate
```

Isso cria o arquivo `db.sqlite3` com as tabelas do sistema (usuários, sessões, etc.).

### 7.2. Criar Superusuário

```bash
python manage.py createsuperuser
```

Forneça:
- **Username:** seu_nome
- **Email:** seu@email.com
- **Password:** (senha segura)

### 7.3. Acessar o Django Admin

Inicie o servidor:
```bash
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000/admin**

O Django Admin é uma interface administrativa poderosa que vem pronta com o Django! 🎉

Você pode:
- Gerenciar usuários e grupos
- Visualizar e editar dados do banco
- Controlar permissões
- (Nas próximas aulas, adicionar seus próprios modelos)

---

## 8. Organizando o Projeto

### 8.1. Estrutura Recomendada

```
meu_projeto/
│
├── venv/                    # Ambiente virtual (não versionar)
├── meu_projeto/             # Configurações do projeto
│   ├── __init__.py
│   ├── settings.py          # ⭐ Configurações principais
│   ├── urls.py              # Roteamento de URLs
│   ├── wsgi.py              # Interface WSGI
│   └── asgi.py              # Interface ASGI
│
├── db.sqlite3               # Banco de dados SQLite
├── manage.py                # Script de gerenciamento
├── requirements.txt         # Dependências Python
└── .gitignore               # Arquivos ignorados pelo Git
```

---

### 8.2. Arquivo .gitignore

Crie um arquivo `.gitignore` na raiz do projeto:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Django
*.log
db.sqlite3
db.sqlite3-journal
media/

# Ambiente Virtual
venv/
env/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Sistema Operacional
.DS_Store
Thumbs.db

# Variáveis de ambiente
.env
```

---

## 9. Boas Práticas

### ✅ Sempre Faça

1. **Use ambiente virtual** para cada projeto
2. **Mantenha requirements.txt atualizado**
3. **Não versione arquivos sensíveis** (senhas, chaves)
4. **Siga convenções de nomenclatura** do Django
5. **Documente seu projeto** (README.md)

### ❌ Evite

1. **Não commite venv/** no Git
2. **Não use DEBUG=True** em produção
3. **Não exponha SECRET_KEY** publicamente
4. **Não commite db.sqlite3** (use migrations)

---

## 10. Comandos Essenciais do Manage.py

```bash
# Servidor
python manage.py runserver

# Banco de dados
python manage.py migrate
python manage.py makemigrations

# Usuários
python manage.py createsuperuser
python manage.py changepassword username

# Outros úteis
python manage.py shell      # Shell Python interativo
python manage.py check      # Verificar problemas no projeto
python manage.py help       # Ver todos os comandos disponíveis
```

---

## 📝 Exercícios Práticos

### Exercício 1: Setup Completo

1. Crie um ambiente virtual chamado `venv`
2. Ative o ambiente virtual
3. Instale Django 5.0
4. Crie um projeto chamado `meu_portfolio`
5. Configure idioma para português e timezone para sua região
6. Execute as migrações iniciais
7. Crie um superusuário
8. Inicie o servidor e acesse no navegador
9. Acesse o Django Admin em `/admin`
10. Crie um arquivo .gitignore
11. Gere o arquivo requirements.txt

### Exercício 2: Explorando Settings

1. Mude o `LANGUAGE_CODE` para 'en-us' e observe a diferença no admin
2. Volte para 'pt-br'
3. Teste diferentes valores de `TIME_ZONE`
4. Documente no README.md quais configurações você alterou

### Exercício 3: Django Admin

1. Faça login no Django Admin
2. Crie 3 novos usuários
3. Crie 2 grupos com nomes "Editores" e "Visitantes"
4. Adicione usuários aos grupos
5. Explore as permissões disponíveis

---

## 🔗 Recursos Adicionais

- [Documentação Oficial Django](https://docs.djangoproject.com/pt-br/5.0/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/pt/)
- [Real Python - Django](https://realpython.com/tutorials/django/)
- [Django Settings Best Practices](https://docs.djangoproject.com/en/5.0/topics/settings/)

---

## 📚 Próxima Aula

Na **Aula 02**, você aprenderá:
- Como criar apps Django
- Sistema de URLs e roteamento
- Views: criando suas primeiras páginas
- Trabalhando com requisições HTTP

---

**Prepare-se para começar a criar páginas web dinâmicas com Django!** 🚀
