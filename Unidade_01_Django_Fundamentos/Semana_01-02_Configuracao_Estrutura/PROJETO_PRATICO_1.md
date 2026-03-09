# Projeto Prático 1 - Configuração de Ambiente e Primeiro Projeto

## 🎯 Objetivo

Configurar corretamente o ambiente de desenvolvimento Django e criar seu primeiro projeto, explorando a estrutura básica e as configurações essenciais do framework.

---

## 📋 Requisitos do Projeto

### O que você vai criar

Um projeto Django básico totalmente configurado e funcional, com:
- Ambiente virtual configurado
- Django instalado e funcionando
- Projeto criado com estrutura completa
- Configurações básicas ajustadas
- Servidor de desenvolvimento rodando
- Documentação do processo

### Requisitos Técnicos

- ✅ Ambiente virtual (venv) criado e ativado
- ✅ Django 5.x instalado
- ✅ Projeto Django criado
- ✅ Configurações em `settings.py` ajustadas
- ✅ Servidor de desenvolvimento funcionando
- ✅ Página de boas-vindas do Django acessível
- ✅ Django Admin acessível
- ✅ Documentação do setup no README.md
- ✅ Arquivo `requirements.txt` gerado

---

## 🗂️ Estrutura do Projeto

```
meu_primeiro_projeto/
├── venv/                      # Ambiente virtual (não versionar)
├── meu_primeiro_projeto/      # Diretório do projeto
│   ├── __init__.py
│   ├── settings.py           # ⭐ Configurações do projeto
│   ├── urls.py               # Mapeamento de URLs
│   ├── asgi.py               # Interface ASGI
│   └── wsgi.py               # Interface WSGI
├── db.sqlite3                # Banco de dados SQLite
├── .gitignore                # Arquivos a ignorar no Git
├── manage.py                 # Script de gerenciamento
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação
```

---

## 🚀 Passo a Passo

### 1. Preparação do Ambiente

#### 1.1. Criar diretório do projeto

```bash
# Criar pasta e entrar nela
mkdir meu_primeiro_projeto
cd meu_primeiro_projeto
```

#### 1.2. Criar e ativar ambiente virtual

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

#### 1.3. Verificar ativação

Você deve ver `(venv)` no início do prompt do terminal.

---

### 2. Instalação do Django

```bash
# Atualizar pip
pip install --upgrade pip

# Instalar Django
pip install django

# Verificar instalação
python -m django --version
```

Você deve ver a versão do Django instalada (ex: 5.1.x).

---

### 3. Criar o Projeto Django

```bash
# Criar projeto no diretório atual
django-admin startproject meu_primeiro_projeto .

# Note o ponto (.) no final - cria no diretório atual
```

#### 3.1. Entender a estrutura criada

```
.
├── manage.py                 # Script principal de gerenciamento
└── meu_primeiro_projeto/     # Pacote Python do projeto
    ├── __init__.py          # Indica que é um pacote Python
    ├── settings.py          # Configurações do projeto
    ├── urls.py              # Mapeamento de URLs
    ├── asgi.py              # Interface ASGI (comunicação assíncrona)
    └── wsgi.py              # Interface WSGI (deploy)
```

---

### 4. Executar Migrações Iniciais

```bash
# Criar banco de dados inicial
python manage.py migrate
```

Isso cria o arquivo `db.sqlite3` com as tabelas do sistema.

---

### 5. Criar Superusuário

```bash
python manage.py createsuperuser
```

Forneça:
- **Username:** seu_nome
- **Email:** seu@email.com
- **Password:** (senha segura)

---

### 6. Executar o Servidor

```bash
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000**

Você deve ver a página de boas-vindas do Django! 🎉

---

### 7. Explorar o Django Admin

Acesse: **http://127.0.0.1:8000/admin**

Faça login com as credenciais do superusuário que você criou.

Explore:
- Interface administrativa
- Gerenciamento de usuários
- Gerenciamento de grupos

> **Nota:** Você aprenderá a criar apps próprios na próxima unidade!

---

### 8. Configurações Importantes

#### 8.1. Ajustar idioma e timezone

Em `settings.py`, localize e modifique:

```python
# Internacionalização
LANGUAGE_CODE = 'pt-br'  # Português do Brasil
TIME_ZONE = 'America/Fortaleza'  # Seu fuso horário
USE_I18N = True
USE_TZ = True
```

#### 8.2. Verificar configurações de debug

```python
# ATENÇÃO: Manter True apenas em desenvolvimento
DEBUG = True

# Hosts permitidos (em desenvolvimento pode ficar assim)
ALLOWED_HOSTS = []
```

---

### 9. Gerar requirements.txt

```bash
pip freeze > requirements.txt
```

Este arquivo lista todas as dependências instaladas.

---

### 10. Criar .gitignore

Crie um arquivo `.gitignore` na raiz do projeto:

```gitignore
# Ambiente virtual
venv/
env/
ENV/

# Banco de dados
*.sqlite3
db.sqlite3

# Arquivos Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Django
*.log
local_settings.py

# Arquivos do sistema
.DS_Store
Thumbs.db

# IDEs
.vscode/
.idea/
*.swp
*.swo
```

---

### 11. Criar README.md

Crie um arquivo `README.md` documentando seu projeto:

```markdown
# Meu Primeiro Projeto Django

## Descrição
Projeto inicial de aprendizado do framework Django.

## Tecnologias
- Python 3.x
- Django 5.x

## Como executar

1. Criar ambiente virtual:
\`\`\`bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
\`\`\`

2. Instalar dependências:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. Executar migrações:
\`\`\`bash
python manage.py migrate
\`\`\`

4. Criar superusuário:
\`\`\`bash
python manage.py createsuperuser
\`\`\`

5. Rodar servidor:
\`\`\`bash
python manage.py runserver
\`\`\`

6. Acessar: http://127.0.0.1:8000

## Admin
- URL: http://127.0.0.1:8000/admin
- Use as credenciais criadas no passo 4

## Autor
[Seu Nome]
```

---

## ✅ Checklist de Conclusão

- [ ] Ambiente virtual criado e ativado
- [ ] Django instalado (verificado com `python -m django --version`)
- [ ] Projeto criado com `django-admin startproject`
- [ ] Entendida a estrutura de diretórios
- [ ] Migrações executadas sem erros
- [ ] Superusuário criado
- [ ] Servidor executando sem erros
- [ ] Página de boas-vindas acessível no navegador
- [ ] Admin acessível e funcional em `/admin`
- [ ] Idioma configurado para pt-br
- [ ] Timezone configurado
- [ ] `requirements.txt` gerado
- [ ] `.gitignore` criado
- [ ] `README.md` criado e documentado

---

## 🎓 O que você aprendeu

✅ Como criar e ativar ambientes virtuais Python  
✅ Como instalar e verificar o Django  
✅ Estrutura básica de um projeto Django  
✅ O que é `manage.py` e seus comandos básicos  
✅ Sistema de migrações do Django  
✅ Como criar superusuário  
✅ Como acessar e usar o Django Admin  
✅ Configurações essenciais em `settings.py`  
✅ Importância do `requirements.txt`  
✅ Boas práticas com `.gitignore`  
✅ Como documentar um projeto  

---

## 📝 Comandos Importantes Aprendidos

```bash
# Ambiente virtual
python -m venv venv                    # Criar
source venv/bin/activate               # Ativar (Linux/Mac)
venv\Scripts\activate                  # Ativar (Windows)
deactivate                             # Desativar

# Django
django-admin startproject nome .       # Criar projeto
python manage.py runserver            # Rodar servidor
python manage.py migrate              # Executar migrações
python manage.py createsuperuser      # Criar superusuário
python manage.py check                # Verificar problemas

# Dependências
pip install django                     # Instalar Django
pip freeze > requirements.txt          # Gerar lista de dependências
pip install -r requirements.txt        # Instalar dependências
```

---

## 🔧 Troubleshooting

### Erro: "command not found: django-admin"
**Solução:** Certifique-se de que o ambiente virtual está ativado.

### Erro: "port already in use"
**Solução:** Outro processo está usando a porta 8000. Tente:
```bash
python manage.py runserver 8001
```

### Erro ao acessar Admin: "no such table"
**Solução:** Execute as migrações:
```bash
python manage.py migrate
```

### Ambiente virtual não ativa no Windows
**Solução:** Pode ser necessário ajustar a política de execução:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📚 Próximos Passos

Após concluir este projeto, você estará pronto para a **Unidade 2**, onde aprenderá:
- [ ] Criar apps Django
- [ ] Sistema de URLs e roteamento
- [ ] Criar suas primeiras views
- [ ] Trabalhar com templates HTML
- [ ] Adicionar arquivos estáticos (CSS, JS, imagens)
- [ ] Construir um site multi-páginas completo

---

## 🎯 Desafio Extra (Opcional)

Se quiser ir além, tente:

1. **Explorar o Django Admin:**
   - Acesse http://127.0.0.1:8000/admin
   - Explore as tabelas de usuários e grupos
   - Tente criar novos usuários pelo admin

2. **Experimentar comandos do Django:**
   ```bash
   python manage.py help           # Ver todos os comandos disponíveis
   python manage.py check          # Verificar problemas no projeto
   python manage.py showmigrations # Ver status das migrações
   python manage.py dbshell        # Abrir shell do banco de dados
   ```

3. **Explorar o settings.py:**
   - Leia os comentários no arquivo
   - Entenda cada configuração
   - Pesquise na documentação sobre cada opção

4. **Testar diferentes configurações:**
   - Mude o `LANGUAGE_CODE` para 'en-us' e veja a diferença
   - Teste com diferentes `TIME_ZONE`
   - Observe as mudanças no admin

---

## 📖 Referências

- [Documentação Oficial do Django](https://docs.djangoproject.com/)
- [Django Tutorial Parte 1](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
- [Python Virtual Environments](https://docs.python.org/3/library/venv.html)

---

**Parabéns! 🎉 Você configurou com sucesso seu primeiro projeto Django!**
