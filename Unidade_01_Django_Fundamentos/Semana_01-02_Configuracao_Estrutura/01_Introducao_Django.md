# Configuração e Estrutura Django - Parte 1

## 🎯 Objetivos de Aprendizagem

Ao final desta aula, você será capaz de:
- Criar e ativar ambientes virtuais Python
- Instalar e configurar o Django
- Compreender a estrutura de um projeto Django
- Criar e organizar apps Django
- Entender o conceito MVT (Model-View-Template)

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

> **Nota:** Você aprenderá mais comandos, incluindo a criação de apps, na próxima unidade!

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

> **Sobre Apps:** Você aprenderá a criar e organizar apps Django na **Unidade 2**, quando trabalharmos com URLs, Views e Templates. Por enquanto, vamos focar na estrutura básica do projeto!

---

## 6. Organização de Projeto

### Estrutura Básica

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

> **Nota:** Na próxima unidade, você aprenderá a adicionar **apps** ao projeto e organizar templates e arquivos estáticos!

---

## 7. Arquivo .gitignore

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

## 8. Boas Práticas

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
4. **Não modifique arquivos do Django** diretamente

---

## 📝 Exercício Prático

### Crie seu primeiro projeto Django:

1. Crie um ambiente virtual chamado `venv`
2. Ative o ambiente virtual
3. Instale Django 5.0
4. Crie um projeto chamado `portfolio`
5. Execute as migrações iniciais
6. Crie um superusuário
7. Inicie o servidor e acesse no navegador
8. Acesse o Django Admin em `/admin`
9. Crie um arquivo .gitignore
10. Gere o arquivo requirements.txt
11. Tire um print da página inicial do Django

---

## 🔗 Recursos Adicionais

- [Documentação Oficial Django](https://docs.djangoproject.com/pt-br/5.0/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/pt/)
- [Real Python - Django](https://realpython.com/tutorials/django/)

---

## 📌 Checklist de Conclusão

Antes de prosseguir, certifique-se de que você:

- [ ] Criou e ativou um ambiente virtual
- [ ] Instalou o Django
- [ ] Criou um projeto Django
- [ ] Executou migrações iniciais
- [ ] Criou um superusuário
- [ ] Iniciou o servidor de desenvolvimento
- [ ] Acessou a página de boas-vindas do Django
- [ ] Acessou o Django Admin
- [ ] Entendeu o conceito de MVT
- [ ] Conhece os comandos básicos do manage.py
- [ ] Criou arquivo .gitignore e requirements.txt

---

**Próxima Aula:** Settings e Configurações Essenciais
