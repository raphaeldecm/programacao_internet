# Planejamento de Ensino - Programação para Internet

## Informações Gerais

**Curso:** Técnico em Informática Integrado ao Ensino Médio  
**Ano/Série:** 4º Ano  
**Disciplina:** Programação para Internet  
**Carga Horária:** 90 horas
**Framework Principal:** Django 5.x (Python)  

### Pré-requisitos (Conhecimentos Esperados):
- ✅ Python (sintaxe, estruturas de dados, funções)
- ✅ Programação Orientada a Objetos
- ✅ HTML5 e CSS3
- ✅ JavaScript básico (variáveis, funções, condicionais, loops)
- ✅ Lógica de programação
- ✅ Git básico (desejável)

### Foco da Disciplina:
Este planejamento foi desenvolvido para turmas que **já possuem base sólida em programação**. O foco está em:
- **Aplicação prática** dos conceitos
- **Desenvolvimento full-stack** com Django
- **Projetos reais** e complexos
- **Integração front-end + back-end**
- **Preparação para o mercado de trabalho**  

---

## Objetivos Gerais

- Desenvolver aplicações web full-stack completas utilizando Django
- Dominar a arquitetura MVT e o ciclo de desenvolvimento com Django
- Implementar APIs RESTful e comunicação assíncrona
- Criar interfaces dinâmicas e responsivas integrando JavaScript com Django
- Aplicar autenticação, autorização e segurança em aplicações web
- Desenvolver projetos reais com deploy e boas práticas de desenvolvimento

---

## Estrutura do Curso (40 semanas letivas)

### **UNIDADE 1: Django - Fundamentos Iniciais** (2 semanas - 4h)

**Conteúdos:**
- Ambientes virtuais e instalação do Django
- Estrutura de projetos e apps
- Settings: configurações essenciais
- Conceitos básicos de arquitetura web

**Atividades Práticas:**
- Setup completo de projeto Django
- Criação de um projeto inicial
- Exploração da estrutura do Django
- **Projeto Prático 1:** Configuração de ambiente e primeiro projeto

---

### **UNIDADE 2: URLs, Views e Protocolo HTTP** (4 semanas - 8h)

**Conteúdos:**
- Sistema de URLs e roteamento
- Views: FBV (Function-Based Views)
- Templates e Django Template Language
- Arquivos estáticos (static files)
- Protocolo HTTP: GET e POST em profundidade
- CSRF Protection

**Atividades Práticas:**
- Criação de múltiplas rotas e views
- Sistema de templates com herança
- **Projeto Prático 2:** Site multi-páginas com navegação

---

### **UNIDADE 3: Models, Banco de Dados e Formulários** (6 semanas - 12h)

#### **Semana 5-6: Models e Banco de Dados**
**Conteúdos:**
- ORM do Django: conceito e vantagens
- Definição de Models e tipos de campos
- Relacionamentos: ForeignKey, ManyToMany, OneToOne
- Migrations: criação e aplicação
- Django Admin: customização básica
- QuerySets: filtros, ordenação e agregação

**Atividades Práticas:**
- Modelagem de banco de dados
- CRUD via shell do Django
- Customização do Django Admin
- Queries complexas

#### **Semana 7-8: Formulários e Validação**
**Conteúdos:**
- Django Forms e ModelForms
- Validação server-side
- Widgets personalizados
- Mensagens de feedback (messages framework)
- Tratamento de erros
- Integração forms + models
- Formulários com relacionamentos

**Atividades Práticas:**
- CRUD completo via formulários
- Validações customizadas
- Upload de arquivos
- **Projeto Prático 3:** Sistema de gerenciamento com CRUD completo

---

### **UNIDADE 4: Class-Based Views e Padrão MVT** (4 semanas - 8h)

#### **Semana 9-10: Class-Based Views (CBV)**
**Conteúdos:**
- Conceito de CBV vs FBV
- Generic Views: ListView, DetailView
- CreateView, UpdateView, DeleteView
- Mixins e herança
- Customização de CBVs
- Padrão MVT na prática
- Separação de responsabilidades

**Atividades Práticas:**
- Refatoração de FBVs para CBVs
- CRUD com generic views
- Paginação e filtros
- **Projeto Prático 4:** Refatoração de sistema existente com CBVs

#### **Semana 11-12: Templates Avançados e Integração Full-Stack**
**Conteúdos:**
- Template tags e filters personalizados
- Inclusão de templates e componentes
- Context processors
- Integração JavaScript + Django Templates
- Passagem de dados Django para JavaScript
- CSRF tokens em AJAX
- Organização de arquivos estáticos

**Atividades Práticas:**
- Componentes reutilizáveis
- Dashboard com gráficos (Chart.js + Django)
- Interface dinâmica com AJAX
- Sistema de busca em tempo real

---

### **UNIDADE 5: Autenticação, Sessões e Controle de Estado** (6 semanas - 12h)

#### **Semana 13-14: Sistema de Autenticação**
**Conteúdos:**
- Sistema de usuários do Django
- User model: padrão e customizado
- Registro, login e logout
- Recuperação de senha
- @login_required e mixins
- Perfis de usuário
- Signals para automação

**Atividades Práticas:**
- Sistema completo de autenticação
- Perfil de usuário com foto
- Recuperação de senha por email
- Personalização do user model

#### **Semana 15-16: Autorização e Permissões**
**Conteúdos:**
- Grupos e permissões
- Permissões customizadas
- Decorators de permissão
- Mixins: PermissionRequiredMixin, UserPassesTestMixin
- Controle de acesso granular
- Auditoria de ações

**Atividades Práticas:**
- Sistema com múltiplos níveis de acesso
- Painel administrativo por função
- Log de atividades dos usuários
- **Projeto Prático 5:** Plataforma multi-usuário com permissões

#### **Semana 17-18: Sessões, Cookies e Controle de Estado**
**Conteúdos:**
- Sessões no Django: configuração e uso
- Armazenamento em sessões
- Cookies: criação e manipulação
- QueryString e parâmetros de URL
- Middleware customizado
- Cache framework
- Estado da aplicação

**Atividades Práticas:**
- Carrinho de compras com sessões
- Sistema de preferências do usuário
- Filtros persistentes
- Implementação de middleware

---

### **UNIDADE 6: APIs REST e Comunicação Assíncrona** (8 semanas - 16h)

#### **Semana 19-20: Django REST Framework - Básico**
**Conteúdos:**
- Conceitos de API REST
- Instalação e configuração do DRF
- Serializers
- APIViews e ViewSets
- Routers
- Autenticação em APIs (Token, JWT)

**Atividades Práticas:**
- API REST para models existentes
- Documentação automática com Swagger
- Teste de endpoints com Postman
- Cliente JavaScript consumindo a API

#### **Semana 21-22: AJAX e Interações Dinâmicas**
**Conteúdos:**
- AJAX com Fetch API
- Requisições assíncronas para Django
- JsonResponse e serialização
- Atualização parcial de páginas
- Upload de arquivos via AJAX
- Tratamento de erros
- Loading states e feedback visual

**Atividades Práticas:**
- Sistema de comentários sem reload
- Like/Unlike assíncrono
- Busca com autocompletar
- Upload de imagens com preview

#### **Semana 23-24: Single Page Application (SPA) com Django**
**Conteúdos:**
- Arquitetura SPA
- Roteamento client-side
- Estado da aplicação no front-end
- Separação API + Front-end
- CORS e configurações
- Autenticação em SPAs

**Atividades Práticas:**
- Mini SPA com JavaScript vanilla
- Dashboard interativo
- **Projeto Prático 6:** Sistema full-stack com API REST

#### **Semana 25-26: WebSockets e Real-Time (Introdução)**
**Conteúdos:**
- Conceito de comunicação real-time
- Django Channels (introdução)
- WebSockets básicos
- Notificações em tempo real
- Chat básico

**Atividades Práticas:**
- Sistema de notificações real-time
- Chat simples
- Atualização automática de dashboards

---

### **UNIDADE 7: Tópicos Avançados e Boas Práticas** (6 semanas - 12h)

#### **Semana 27-28: Segurança e Performance**
**Conteúdos:**
- OWASP Top 10
- SQL Injection e ORM protection
- XSS e CSRF protection
- Validação e sanitização de dados
- HTTPS e configurações de segurança
- Query optimization (select_related, prefetch_related)
- Cache strategies
- Compressão e minificação

**Atividades Práticas:**
- Auditoria de segurança
- Otimização de queries lentas
- Implementação de cache
- Debug toolbar e profiling

#### **Semana 29-30: Testing e Qualidade de Código**
**Conteúdos:**
- Testes unitários com unittest/pytest
- Testes de integração
- Testes de views e models
- Coverage de testes
- TDD (Test-Driven Development)
- Fixtures e factories
- Linting e formatação (Black, Flake8)

**Atividades Práticas:**
- Criação de suite de testes
- TDD em funcionalidades novas
- Configuração de CI/CD básico
- Code review colaborativo

#### **Semana 31-32: Deployment e DevOps**
**Conteúdos:**
- Preparação para produção
- Variáveis de ambiente
- Banco de dados PostgreSQL
- Servidor de aplicação (Gunicorn)
- Servidor web (Nginx)
- Deploy em plataformas (Railway, Render, PythonAnywhere)
- Git e GitHub Actions
- Monitoramento básico

**Atividades Práticas:**
- Configuração de ambiente de produção
- Deploy de aplicação completa
- Configuração de domínio
- Backup e restore de dados

---

### **UNIDADE 8: Projeto Final Integrador** (6 semanas - 12h)

#### **Semana 33-38: Desenvolvimento do Projeto Final**
**Metodologia:**
- Trabalho em duplas ou trios
- Metodologia ágil (Scrum simplificado)
- Sprints semanais com apresentações
- Code review entre equipes
- Documentação técnica
- Apresentação final

**Requisitos do Projeto:**
- Sistema full-stack Django + JavaScript
- Mínimo 5 models com relacionamentos
- API REST funcional
- Autenticação e autorização
- CRUD completo para todas entidades
- Interface responsiva e interativa
- Validações client-side e server-side
- Testes automatizados (mínimo 70% coverage)
- Deploy em produção
- Documentação técnica (README, API docs)
- Apresentação de 15 minutos

**Cronograma do Projeto:**
- **Semana 33:** Planejamento, definição de requisitos e modelagem
- **Semana 34:** Desenvolvimento do back-end (models, views, API)
- **Semana 35:** Desenvolvimento do front-end e integrações
- **Semana 36:** Testes, refatoração e melhorias
- **Semana 37:** Deploy, documentação e ajustes finais
- **Semana 38:** Apresentações finais e avaliação por pares

### Sugestões de Projetos (em ordem de complexidade):

#### **Nível Intermediário:**
1. **Sistema de Biblioteca Digital**
   - Catálogo de livros com busca avançada
   - Empréstimos e devoluções
   - Perfis de usuários (admin, bibliotecário, leitor)
   - Notificações de atraso
   - Dashboard com estatísticas

2. **Plataforma de Cursos Online (LMS simplificado)**
   - Cadastro de cursos e módulos
   - Matrículas de alunos
   - Acompanhamento de progresso
   - Fórum de discussão
   - Certificados automáticos

3. **Sistema de Help Desk**
   - Abertura de chamados
   - Sistema de prioridades
   - Atribuição de técnicos
   - Histórico de atendimentos
   - Dashboard de métricas

#### **Nível Avançado:**
4. **E-commerce Completo**
   - Catálogo de produtos com categorias
   - Carrinho de compras
   - Sistema de pagamento (simulado)
   - Painel de vendedor
   - Sistema de avaliações
   - Wishlist e comparação de produtos

5. **Rede Social Temática**
   - Sistema de posts e comentários
   - Seguir/deixar de seguir usuários
   - Feed personalizado
   - Notificações em tempo real
   - Mensagens privadas
   - Sistema de hashtags

6. **Sistema de Gerenciamento de Projetos**
   - Projetos e tarefas
   - Quadro Kanban
   - Atribuição de membros
   - Calendário de atividades
   - Comentários e anexos
   - Relatórios de progresso

---

### **REVISÃO OPCIONAL: JavaScript Moderno** (4 semanas - 8h)
> **Nota:** Este conteúdo pode ser ministrado ao final da disciplina (semanas 39-40) se houver tempo disponível, ou integrado de forma prática durante a UNIDADE 6 (APIs e AJAX).

#### **JavaScript ES6+ e Manipulação do DOM** (2 semanas)
**Conteúdos:**
- Revisão rápida: let/const, arrow functions, destructuring, spread operator
- Template literals e interpolação
- Métodos modernos de arrays: map, filter, reduce, find, some, every
- Promises e async/await
- Fetch API para requisições HTTP
- Manipulação avançada do DOM
- Event delegation e listeners
- Validação de formulários dinâmica

**Atividades Práticas:**
- Consumo de API pública (ViaCEP, IBGE)
- Validação client-side com feedback visual
- Sistema de busca com filtros dinâmicos

#### **JavaScript Assíncrono e AJAX** (2 semanas)
**Conteúdos:**
- Comunicação assíncrona cliente-servidor
- Requisições GET, POST, PUT, DELETE com Fetch
- Tratamento de respostas JSON
- Manipulação de erros e loading states
- LocalStorage e SessionStorage
- Integração JavaScript + HTML/CSS
- Boas práticas de organização de código JS

**Atividades Práticas:**
- CRUD client-side com LocalStorage
- Interface SPA (Single Page Application) simples
- Sistema de notificações dinâmicas
- Dashboard interativo com dados persistentes

---

## 📊 Metodologia de Ensino

### Abordagem Pedagógica (Foco em Aplicação Prática):
- **Aulas expositivas** breves com conceitos (20%)
- **Live coding** e demonstrações práticas (30%)
- **Hands-on em laboratório** - desenvolvimento guiado (35%)
- **Projetos práticos** e desafios (15%)

### Estratégias de Ensino:
- **Flipped Classroom:** leitura prévia de documentação, aula para prática
- **Pair Programming:** desenvolvimento em duplas
- **Code Review:** análise colaborativa de código
- **Sprint Projects:** projetos curtos com entregas semanais
- **Tech Talks:** apresentações de soluções pelos alunos

### Recursos e Ferramentas:
- **IDE:** VS Code com extensões (Python, Django, ESLint, Prettier)
- **Versionamento:** Git/GitHub com GitHub Classroom
- **Banco de Dados:** SQLite (dev) / PostgreSQL (prod)
- **API Testing:** Postman/Insomnia/Thunder Client
- **Deploy:** Railway, Render ou PythonAnywhere
- **Colaboração:** Discord/Slack para comunicação
- **Documentação:** Notion/GitHub Wiki para materiais

---

## 📈 Avaliação

### Distribuição de Pontos por Bimestre:

#### **1º Bimestre (25 pontos)**
- **Projeto Prático 1** - Site multi-páginas Django (10 pontos)
- **Projeto Prático 2** - CRUD completo (10 pontos)
- **Exercícios e desafios** (3 pontos)
- **Participação e code review** (2 pontos)

#### **2º Bimestre (25 pontos)**
- **Projeto Prático 3** - Refatoração com CBVs (8 pontos)
- **Projeto Prático 4** - Plataforma multi-usuário (12 pontos)
- **Avaliação prática** - Implementação de funcionalidade (3 pontos)
- **Atividades em laboratório** (2 pontos)

#### **3º Bimestre (25 pontos)**
- **Projeto Prático 5** - Sistema com API REST (15 pontos)
- **Desafios de código** (5 pontos)
- **Testes e documentação** (5 pontos)

#### **4º Bimestre (25 pontos)**
- **Projeto Final** (18 pontos)
  - Funcionalidade e requisitos (7 pontos)
  - Qualidade de código e testes (5 pontos)
  - Interface e UX (3 pontos)
  - Documentação (3 pontos)
- **Apresentação** (4 pontos)
- **Avaliação por pares** (3 pontos)

### Critérios Detalhados de Avaliação dos Projetos:

#### **Funcionalidade (35%)**
- Todos os requisitos implementados
- Sistema estável sem crashes
- Casos de uso funcionam corretamente
- Tratamento adequado de erros

#### **Qualidade de Código (30%)**
- Organização e estrutura clara
- Nomenclatura consistente
- Código DRY (Don't Repeat Yourself)
- Boas práticas Django e JavaScript
- Comentários em partes complexas
- Testes automatizados (quando aplicável)

#### **Interface e UX (20%)**
- Design responsivo
- Usabilidade intuitiva
- Feedback visual adequado
- Acessibilidade básica
- Loading states e tratamento de erros

#### **Inovação e Extras (10%)**
- Funcionalidades além do requisitado
- Soluções criativas para problemas
- Uso de tecnologias complementares
- Polimento e atenção aos detalhes

#### **Documentação (5%)**
- README completo
- InstEstratégias para Maximizar o Aprendizado

### Para o Professor:

#### **Aulas Práticas:**
- Equilibre conceitos e aplicação (20/80)
- Use live coding com exemplos reais
- Apresente o problema antes da solução
- Incentive debugging colaborativo
- Faça code reviews ao vivo
- Compartilhe repositório de exemplos

#### **Engajamento:**
- Crie desafios semanais opcionais
- Gamifique com badges e conquistas
- Organize mini-hackathons bimestrais
- Convide ex-alunos ou profissionais
- MoEssencial (Documentação Oficial):
1. **Documentação Django** (PT-BR) - https://docs.djangoproject.com/pt-br/
2. **Django REST Framework** - https://www.django-rest-framework.org/
3. **MDN Web Docs - JavaScript** - https://developer.mozilla.org/pt-BR/
4. **JavaScript.info** - https://javascript.info/ (moderno e completo)

### Livros Recomendados:
5. **Two Scoops of Django** - Daniel e Audrey Roy Greenfeld (boas práticas)
6. **Django for Professionals** - William S. Vincent (avançado)
7. **Eloquent JavaScript** - Marijn Haverbeke (online gratuito)
8. **Django for APIs** - William S. Vincent (DRF)

### Tutoriais e Cursos Online:
9. **Django Girls Tutorial** - https://tutorial.djangogirls.org/pt/ (introdução)
10. **Real Python Django** - https://realpython.com/tutorials/django/
11. **Django Framework na Prática** - Material GitHub disponível
12. **FreeCodeCamp** - JavaScript e back-end

### Recursos para Prática:
13. **Django Packages** - https://djangopackages.org/ (pacotes úteis)
14. **Awesome Django** - https://github.com/wsvincent/awesome-django
15. **Django Project Examples** - GitHub (projetos reais)
16. **HackerRank** - Desafios de programação

---

## 🔄 Flexibilidade e Ajustes

### Considerações Importantes:

**Conhecimento Prévio (já contemplado):**
- ✅ Python e OOP: assumido domínio
- ✅ HTML/CSS: revisão mínima apenas
- ✅ JavaScript básico: foco no moderno e avançado

### Possíveis Ajustes Durante o Ano:

#### **Se a turma avançar rapidamente:**
- Introduzir **Django REST Framework** mais cedo (semana 17)
- Adicionar **React/Vue.js básico** (2 semanas)
- Implementar **WebSockets completo** com chat
- Explorar **containerização com Docker**
- Aprofundar em **CI/CD e DevOps**

#### **Se houver dificuldades:**
- Estender **UNIDADE 1** em 1-2 semanas (mais prática com Models)
- Adicionar mais exercícios guiados nas **UNIDADES 3 e 4**
- Simplificar requisitos do **Projeto Final**
- Oferecer aulas de reforço paralelas

#### **Adaptações ao Calendário:**
- Planejamento considera 36 semanas letivas obrigatórias + 4 opcionais
- Ajuste para feriados e eventos escolares
- Marque sprints de projetos antes de avaliações
- Evite novos conteúdos em semanas de provas de outras disciplinas

### Conteúdos Opcionais/Bonus:

**Para alunos avançados:**
- Frameworks JavaScript (React, Vue.js, Alpine.js)
- GraphQL como alternativa a REST
- Docker e containerização
- Tailwind CSS e componentes modernos
- Celery para tarefas assíncronas
- Elasticsearch para busca avançada
- Stripe API para pagamentos reais

---

## 📅 Cronograma Resumido

| Período | Unidade | Foco Principal | Projeto Prático |
|---------|---------|----------------|-----------------|
| Semanas 1-6 | **UN1:** Django Fundamentos | MVT, Models, Forms | Site multi-páginas + CRUD |
| Semanas 7-10 | **UN2:** CBVs e MVT | Class-Based Views | Refatoração + Dashboard |
| Semanas 11-16 | **UN3:** Auth & Estado | Autenticação, Permissões, Sessões | Plataforma multi-usuário |
| Semanas 17-24 | **UN4:** APIs REST | DRF, AJAX, SPA, Real-time | Sistema com API REST |
| Semanas 25-30 | **UN5:** Avançado | Segurança, Testes, Deploy | Otimização e Deploy |
| Semanas 31-36 | **UN6:** Projeto Final | Integração Full-Stack | **Projeto Integrador** |
| Semanas 37-40 | **Revisão Opcional** | JavaScript ES6+ | Integração front-end |

> **Observação:** As semanas 37-40 são opcionais e destinadas à revisão de JavaScript moderno, caso haja tempo disponível.

### Distribuição de Carga Horária:

```
Django Fundamentos:        12h  (15%)
Class-Based Views:          8h  (10%)
Auth & Controle Estado:    12h  (15%)
APIs e Comunicação:        16h  (20%)
Tópicos Avançados:         12h  (15%)
Projeto Final:             12h  (15%)
JavaScript (Opcional):      8h  (10%)
                          ----
Total:                     80h
```

### Marcos Importantes (Milestones):

- **Semana 6:** Primeiro sistema Django full CRUD
- **Semana 10:** Domínio de Class-Based Views
- **Semana 16:** Sistema completo com autenticação
- **Semana 24:** API REST funcional com SPA
- **Semana 30:** Deploy em produção com testes
- **Semana 36:** Projeto Final apresentado
- **Semana 40 (opcional):** Revisão JavaScript concluída

---

## 🎓 Competências Desenvolvidas

Ao final da disciplina, os alunos serão capazes de:

### Técnicas:
✅ Desenvolver aplicações web full-stack completas  
✅ Implementar APIs RESTful profissionais  
✅ Criar interfaces dinâmicas e responsivas  
✅ Aplicar autenticação e autorização robustas  
✅ Modelar e manipular bancos de dados relacionais  
✅ Escrever código limpo e testável  
✅ Fazer deploy de aplicações em produção  
✅ Debugar e otimizar aplicações web  

### Profissionais:
✅ Trabalhar em equipe usando Git/GitHub  
✅ Seguir metodologias ágeis  
✅ Documentar código e APIs  
✅ Apresentar soluções técnicas  
✅ Resolver problemas de forma autônoma  
✅ Aprender novas tecnologias continuamente  

---

## 📞 Recursos de Apoio

### Comunicação:
- **Discord/Slack:** Canal da turma para dúvidas
- **GitHub Classroom:** Repositório de materiais e exercícios
- **Office Hours:** Horários de atendimento do professor

### Materiais Complementares:
- Repositório com exemplos de código
- Vídeo-aulas gravadas
- Cheat sheets de Django e JavaScript
- Templates de projeto
- Lista de exercícios extras

### Comunidades:
- Django Brasil (Telegram/Discord)
- Python Brasil
- Stack Overflow em Português
- Reddit r/django
- Dev.to

---

**Elaborado em:** 26 de fevereiro de 2026  
**Público-alvo:** 4º ano - Técnico em Informática Integrado  
**Pré-requisitos:** Python, OOP, HTML/CSS, JavaScript básico  
**Revisão:** A ser realizada ao final de cada bimestre com feedback da turma
- Docker e containerização
- Tailwind CSS e componentes modernos
- Celery para tarefas assíncronas
- Elasticsearch para busca avançada
- Stripe API para pagamentos reais
#### **Aprendizado Efetivo:**
- Leia a documentação oficial
- Não copie código sem entender
- Debug antes de buscar ajuda
- Explique seu código para alguém (rubber duck)
- Mantenha anotações e snippets úteis

#### **Construção de Portfólio:**
- Todos os projetos no GitHub
- README detalhado em cada projeto
- Deploy de pelo menos 3 projetos
- Documente seu aprendizado (blog/Medium)
- Participe de comunidades (Discord, Reddit)

#### **Soft Skills:**
- Trabalhe em equipe efetivamente
- Pratique pair programming
- Faça code reviews com colegas
- Apresente suas soluções
- Peça e dê feedback construtivamenteial.djangogirls.org/pt/
2. **MDN Web Docs - JavaScript** - https://developer.mozilla.org/pt-BR/docs/Web/JavaScript
3. **Documentação Oficial Django** - https://docs.djangoproject.com/pt-br/

### Complementar:
4. **JavaScript: O Guia Definitivo** - David Flanagan
5. **Two Scoops of Django** - Daniel e Audrey Roy Greenfeld
6. **Eloquent JavaScript** - Marijn Haverbeke (disponível online gratuitamente)

### Online:
7. **FreeCodeCamp** - Exercícios práticos de JavaScript
8. **Django for Beginners** - William S. Vincent
9. **JavaScript.info** - Tutorial moderno de JavaScript

---

## 💡 Dicas para o Sucesso da Disciplina

### Para o Professor:
- Equilibre teoria e prática (30/70)
- Use exemplos do cotidiano dos alunos
- Incentive a resolução de problemas reais
- Promova pair programming
- Utilize code reviews nas atividades
- Mantenha um repositório de exemplos no GitHub
- Crie um canal de comunicação (Discord/Slack) para dúvidas

### Para os Alunos:
- Pratique código todos os dias (mesmo que 30 minutos)
- Não copie e cole código sem entender
- Use o DevTools para debugar
- Documente seu código
- Participe de comunidades online
- Construa um portfólio no GitHub
- Tente projetos pessoais além dos propostos

---

## 🔄 Observações e Flexibilidade

Este planejamento pode ser ajustado conforme:
- **Ritmo da turma**: algumas turmas podem precisar de mais tempo em certos tópicos
- **Conhecimento prévio**: se a turma já tem experiência com Python, acelere a Unidade 3
- **Calendário escolar**: ajuste para feriados e eventos da escola
- **Feedback dos alunos**: adapte metodologia conforme resposta da turma
- **Atualizações tecnológicas**: Django e JavaScript evoluem constantemente

### Ajustes Sugeridos:
- Se a turma tem dificuldade com JavaScript, adicione 2 semanas na Unidade 1
- Se a turma já conhece Python bem, reduza a Unidade 3 para 6 semanas
- Considere introduzir frameworks JavaScript modernos (React/Vue) como conteúdo extra

---

## 📅 Cronograma Resumido

| Período | Unidade | Conteúdo Principal | Projeto |
|---------|---------|-------------------|---------|
| Semanas 1-10 | Unidade 1 | JavaScript Fundamentals | To-Do List |
| Semanas 11-16 | Unidade 2 | DOM e Eventos | Página Interativa |
| Semanas 17-24 | Unidade 3 | Django Básico | Sistema de Cadastro |
| Semanas 25-28 | Unidade 4 | Estado e Sessões | Carrinho de Compras |
| Semanas 29-32 | Unidade 5 | Autenticação | Sistema com Login |
| Semanas 33-38 | Unidade 6 | Banco de Dados | Sistema de Gerenciamento |
| Semanas 39-40 | Unidade 7 | MVC/MVT | Projeto Final |

---

**Elaborado em:** 26 de fevereiro de 2026  
**Revisão:** A ser realizada ao final de cada bimestre
