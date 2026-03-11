# Programação para Internet - Django

Este repositório contém o material didático da disciplina de Programação para Internet, com foco no desenvolvimento web utilizando o framework Django.

## Sobre a Disciplina

Esta disciplina é ministrada no **Curso Técnico em Informática do IFRN (Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte)**.

A disciplina aborda os conceitos fundamentais e práticos do desenvolvimento web moderno utilizando Python e o framework Django, capacitando os alunos a criar aplicações web robustas, escaláveis e seguras.

## Objetivos

- Compreender os fundamentos de desenvolvimento web
- Dominar a arquitetura MVT (Model-View-Template) do Django
- Desenvolver aplicações web completas e funcionais
- Implementar autenticação, autorização e segurança
- Trabalhar com bancos de dados relacionais através do Django ORM
- Criar APIs RESTful utilizando Django REST Framework
- Aplicar boas práticas de desenvolvimento web

## Estrutura do Repositório

O conteúdo está organizado por aulas sequenciais, cada uma com seu material teórico, projeto prático e referências:

```
programacao_internet/
├── README.md
├── Planejamento_Disciplina.md
├── Materiais_de_Estudo.md
├── Aula_01_Introducao_Django/
│   ├── conteudo.md           # Material teórico
│   ├── projeto_pratico.md    # Atividade prática
│   └── referencia_rapida.md  # Referência rápida
├── Aula_02_URLs_Views/
│   ├── conteudo.md
│   └── projeto_pratico.md
├── Aula_03_Templates/
│   ├── conteudo.md
│   └── projeto_pratico.md
└── Aula_04_JavaScript_Django/
    ├── conteudo.md
    └── projeto_pratico.md
```

### 📚 Conteúdo das Aulas

#### **Aula 01 - Introdução ao Django**
- Ambientes virtuais (venv)
- Instalação do Django
- Estrutura de um projeto Django
- Padrão MVT (Model-View-Template)
- Arquivo settings.py e configurações
- Django Admin
- **Projeto Prático:** Configuração de ambiente e primeiro projeto

#### **Aula 02 - URLs e Views**
- Criando apps Django
- Sistema de URLs e roteamento
- Path converters e parâmetros
- Function-Based Views (FBV)
- Objeto Request e Response
- Métodos HTTP (GET vs POST)
- CSRF Protection
- **Projeto Prático:** Site multi-páginas

#### **Aula 03 - Templates**
- Django Template Language (DTL)
- Herança de templates
- Tags ({% for %}, {% if %}, {% url %})
- Filtros (date, truncatewords, etc)
- Arquivos estáticos (CSS, JS, imagens)
- Partials e includes
- **Projeto Prático:** Blog com templates

#### **Aula 04 - JavaScript com Django**
- Integrando JavaScript nos templates
- Fetch API e requisições assíncronas
- AJAX com Django
- Criando APIs JSON
- Manipulação do DOM
- Interações dinâmicas
- **Projeto Prático:** To-Do List com JavaScript

## Tecnologias

- **Python** - Linguagem de programação
- **Django** - Framework web
- **HTML/CSS/JavaScript** - Frontend
- **SQLite/PostgreSQL** - Banco de dados
- **Git** - Controle de versão

## Pré-requisitos

- Conhecimento básico de Python
- Noções de HTML e CSS
- Ambiente de desenvolvimento Python configurado
- Git instalado

## Como Começar

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd programacao_internet
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências (quando disponíveis):
```bash
pip install -r requirements.txt
```

## Material de Apoio

- [Documentação Oficial do Django](https://docs.djangoproject.com/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [MDN Web Docs](https://developer.mozilla.org/)

## Licença

Este material é disponibilizado para fins educacionais.

## Contato

**Professor:** Raphael Muniz  
**E-mail:** raphael.muniz@ifrn.edu.br

Para dúvidas e sugestões sobre o material da disciplina, entre em contato através dos canais oficiais do IFRN.

---

**Última atualização:** Fevereiro de 2026
