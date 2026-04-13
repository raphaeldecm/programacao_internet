# Sistema de Gerenciamento de Mercado

Sistema web desenvolvido em Django para gerenciamento completo de operações de um mercado, incluindo produtos, clientes, vendas, compras e usuários.

## 📋 Descrição

Este projeto é uma aplicação web moderna e responsiva para gerenciar as operações de um mercado. O sistema oferece um dashboard intuitivo com visualização de dados em tempo real, gestão de estoque, controle de vendas e compras, além de gerenciamento de clientes e usuários.

## ✨ Funcionalidades

- **Dashboard Interativo**: Painel de controle com métricas e gráficos em tempo real
  - Estatísticas de produtos, clientes, vendas e compras
  - Gráficos de vendas mensais
  - Visualização de produtos mais vendidos
  - Tabela de últimas transações

- **Gestão de Produtos**: Cadastro, edição e listagem de produtos
- **Gestão de Clientes**: Controle completo de clientes
- **Vendas**: Registro e acompanhamento de vendas
- **Compras**: Controle de compras e fornecedores
- **Usuários**: Sistema de autenticação e gerenciamento de usuários
- **Interface Responsiva**: Design moderno e minimalista que se adapta a diferentes dispositivos

## 🚀 Tecnologias Utilizadas

- **Backend**: Python 3.x / Django 6.0.4
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Banco de Dados**: SQLite3
- **Gráficos**: Canvas API
- **Design**: CSS Grid, Flexbox, Variáveis CSS

## 📁 Estrutura do Projeto

```
Projeto/
├── mercado/                # Configurações do projeto Django
│   ├── settings.py        # Configurações gerais
│   ├── urls.py           # Rotas principais
│   └── wsgi.py           # Configuração WSGI
├── produtos/             # App de produtos
│   ├── models.py         # Modelos de dados
│   ├── views.py          # Lógica de visualização
│   ├── urls.py           # Rotas do app
│   └── admin.py          # Configuração do admin
├── static/               # Arquivos estáticos
│   ├── css/
│   │   └── style.css     # Estilos principais
│   ├── js/
│   │   └── style.js      # Scripts JavaScript
│   └── img/              # Imagens
├── templates/            # Templates HTML
│   └── home.html         # Dashboard principal
├── db.sqlite3           # Banco de dados SQLite
├── manage.py            # Gerenciador do Django
└── README.md            # Este arquivo
```

## 🛠️ Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- virtualenv (recomendado)

### Passos para instalação

1. **Clone o repositório** (ou navegue até o diretório do projeto):
   ```bash
   cd /caminho/para/programacao_internet/Projeto
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install django
   ```

4. **Execute as migrações do banco de dados**:
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário** (opcional):
   ```bash
   python manage.py createsuperuser
   ```

6. **Colete arquivos estáticos** (se necessário):
   ```bash
   python manage.py collectstatic --noinput
   ```

## ▶️ Como Executar

1. **Inicie o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

2. **Acesse a aplicação**:
   - Dashboard: http://127.0.0.1:8000/
   - Produtos: http://127.0.0.1:8000/produtos/
   - Admin: http://127.0.0.1:8000/admin/

## 🎨 Design e Interface

O sistema foi desenvolvido com foco em:
- **Minimalismo**: Interface limpa e intuitiva
- **Cores claras**: Paleta de cores suaves e profissionais
- **Responsividade**: Adaptação para desktop, tablet e mobile
- **Acessibilidade**: Elementos bem estruturados e legíveis

### Paleta de Cores

- Primary: `#6366f1` (Índigo)
- Secondary: `#8b5cf6` (Roxo)
- Success: `#10b981` (Verde)
- Warning: `#f59e0b` (Laranja)
- Danger: `#ef4444` (Vermelho)
- Background: `#f8fafc` (Cinza claro)

## 📱 Funcionalidades Mobile

- Menu lateral retrátil
- Layout responsivo com grid adaptativo
- Overlay para navegação mobile
- Tipografia otimizada para telas pequenas

## 🔐 Autenticação

O sistema possui controle de acesso com autenticação de usuários. Para acessar funcionalidades protegidas, é necessário realizar login.

## 🛣️ Rotas Principais

| Rota | Descrição |
|------|-----------|
| `/` | Dashboard principal |
| `/produtos/` | Lista de produtos |
| `/admin/` | Painel administrativo Django |

## 📊 Funcionalidades do Dashboard

- **Cards de Estatísticas**: Visualização rápida de métricas importantes
- **Gráfico de Vendas Mensais**: Acompanhamento de vendas ao longo do ano
- **Produtos Mais Vendidos**: Ranking de produtos
- **Últimas Transações**: Histórico recente de operações

## 🔧 Configurações

As configurações do projeto estão em `mercado/settings.py`:
- Idioma: Português (pt-br)
- Timezone: America/Sao_Paulo
- Debug: True (modo desenvolvimento)
- Static Files: Configurados em `/static/`

## 📝 Próximas Funcionalidades

- [ ] Sistema completo de autenticação e autorização
- [ ] CRUD completo de clientes
- [ ] Módulo de vendas com carrinho
- [ ] Módulo de compras e fornecedores
- [ ] Relatórios em PDF
- [ ] Gráficos mais avançados com bibliotecas especializadas
- [ ] Sistema de notificações
- [ ] API REST para integração
- [ ] Testes automatizados

## 👨‍💻 Desenvolvimento

Para contribuir com o projeto:

1. Crie uma branch para sua feature: `git checkout -b feature/nova-funcionalidade`
2. Faça commit das mudanças: `git commit -m 'Adiciona nova funcionalidade'`
3. Envie para a branch: `git push origin feature/nova-funcionalidade`
4. Abra um Pull Request

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte da disciplina de Programação para Internet.

## 📧 Contato

Para dúvidas ou sugestões sobre o projeto, entre em contato.

---

**Desenvolvido com ❤️ usando Django**
