# Aula 04 - JavaScript com Django em Templates

## 🎯 Objetivos de Aprendizagem

Ao final desta aula, você será capaz de:
- Integrar JavaScript com templates Django
- Fazer requisições assíncronas com Fetch API
- Trabalhar com JSON no Django
- Implementar funcionalidades dinâmicas sem recarregar a página
- Criar APIs simples com Django
- Manipular o DOM com dados do servidor

---

## 1. Integrando JavaScript nos Templates

### 1.1. Formas de Adicionar JavaScript

**Inline (dentro do HTML):**
```html
<button onclick="alert('Olá!')">Clique Aqui</button>
```

**Tag script no template:**
```html
<script>
    console.log('JavaScript no template');
</script>
```

**Arquivo externo (recomendado):**
```html
{% load static %}
<script src="{% static 'js/script.js' %}"></script>
```

### 1.2. Onde Colocar o JavaScript

**No final do `<body>` (recomendado):**
```html
{% extends 'base.html' %}

{% block content %}
    <div id="app">
        <!-- conteúdo -->
    </div>
{% endblock %}

{% block extra_js %}
<script src="{% static 'app/js/app.js' %}"></script>
{% endblock %}
```

**Por quê no final?** O JavaScript carrega após o HTML, evitando erros ao tentar manipular elementos que ainda não existem.

---

## 2. JavaScript Básico para Django

### 2.1. Selecionando Elementos

```javascript
// Por ID
const botao = document.getElementById('meu-botao');

// Por classe
const cards = document.getElementsByClassName('card');

// Query selector (mais moderno)
const botao = document.querySelector('#meu-botao');
const cards = document.querySelectorAll('.card');
```

### 2.2. Event Listeners

```javascript
// Click
botao.addEventListener('click', function() {
    console.log('Botão clicado!');
});

// Submit de formulário
const form = document.querySelector('#meu-form');
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Previne reload da página
    console.log('Formulário enviado!');
});

// Input
const input = document.querySelector('#busca');
input.addEventListener('input', function(event) {
    console.log('Valor:', event.target.value);
});
```

### 2.3. Manipulando o DOM

```javascript
// Alterar conteúdo
elemento.textContent = 'Novo texto';
elemento.innerHTML = '<strong>HTML</strong>';

// Alterar estilos
elemento.style.color = 'red';
elemento.style.display = 'none';

// Adicionar/remover classes
elemento.classList.add('ativo');
elemento.classList.remove('inativo');
elemento.classList.toggle('expandido');

// Criar elementos
const div = document.createElement('div');
div.textContent = 'Nova div';
document.body.appendChild(div);
```

---

## 3. Django + JavaScript: Passando Dados

### 3.1. Do Django para JavaScript (JSON)

**View:**
```python
def minha_view(request):
    dados = {
        'usuario': 'João',
        'idade': 25,
        'itens': ['Item 1', 'Item 2', 'Item 3']
    }
    return render(request, 'pagina.html', {'dados': dados})
```

**Template:**
```html
<script>
    // Usando json_script filter
    const dados = JSON.parse(document.getElementById('dados-json').textContent);
    console.log(dados);
</script>

{{ dados|json_script:"dados-json" }}
```

**Resultado:**
```html
<script id="dados-json" type="application/json">
{"usuario": "João", "idade": 25, "itens": ["Item 1", "Item 2", "Item 3"]}
</script>
```

### 3.2. URLs do Django no JavaScript

```html
<script>
    // URL estática
    const url = "{% url 'blog:lista' %}";
    console.log(url); // "/blog/"
    
    // URL com parâmetros
    const postId = 5;
    const urlDetalhe = `/blog/${postId}/`;
    
    // Melhor: usar data attributes
    const botao = document.querySelector('#botao-deletar');
    const deleteUrl = botao.dataset.url;
</script>

<button id="botao-deletar" data-url="{% url 'blog:deletar' post_id=post.id %}">
    Deletar
</button>
```

---

## 4. CSRF Token em Requisições JavaScript

### 4.1. Obtendo o Token

```javascript
// Função para pegar o CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');
```

### 4.2. Usando o Token nas Requisições

```javascript
fetch('/api/endpoint/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({
        chave: 'valor'
    })
});
```

---

## 5. Fetch API - Requisições Assíncronas

### 5.1. GET Request

```javascript
// Buscar dados
fetch('/api/posts/')
    .then(response => response.json())
    .then(data => {
        console.log('Dados recebidos:', data);
        // Fazer algo com os dados
    })
    .catch(error => {
        console.error('Erro:', error);
    });
```

### 5.2. POST Request

```javascript
const csrftoken = getCookie('csrftoken');

fetch('/api/posts/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({
        titulo: 'Novo Post',
        conteudo: 'Conteúdo do post'
    })
})
.then(response => response.json())
.then(data => {
    console.log('Post criado:', data);
})
.catch(error => {
    console.error('Erro:', error);
});
```

### 5.3. Com async/await (moderno)

```javascript
async function buscarPosts() {
    try {
        const response = await fetch('/api/posts/');
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Erro:', error);
    }
}

// Usar
buscarPosts();
```

---

## 6. Criando uma API JSON no Django

### 6.1. View que Retorna JSON

```python
from django.http import JsonResponse

def api_posts(request):
    posts = [
        {'id': 1, 'titulo': 'Post 1', 'autor': 'João'},
        {'id': 2, 'titulo': 'Post 2', 'autor': 'Maria'},
    ]
    return JsonResponse({'posts': posts})

def api_post_detalhe(request, post_id):
    post = {'id': post_id, 'titulo': 'Meu Post', 'autor': 'João'}
    return JsonResponse(post)
```

### 6.2. View que Aceita POST

```python
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def api_posts(request):
    if request.method == 'GET':
        # Listar posts
        posts = [...]
        return JsonResponse({'posts': posts})
    
    elif request.method == 'POST':
        # Criar post
        data = json.loads(request.body)
        titulo = data.get('titulo')
        conteudo = data.get('conteudo')
        
        # Processar (salvar no banco, etc)
        
        return JsonResponse({
            'success': True,
            'message': 'Post criado com sucesso!',
            'post': {
                'id': 1,
                'titulo': titulo,
                'conteudo': conteudo
            }
        })
```

---

## 7. Exemplos Práticos

### 7.1. Busca Dinâmica (Sem Recarregar Página)

**Template:**
```html
<input type="text" id="busca" placeholder="Buscar posts...">
<div id="resultados"></div>

<script>
const inputBusca = document.getElementById('busca');
const divResultados = document.getElementById('resultados');

inputBusca.addEventListener('input', async function(e) {
    const query = e.target.value;
    
    if (query.length < 3) {
        divResultados.innerHTML = '';
        return;
    }
    
    try {
        const response = await fetch(`/api/buscar/?q=${query}`);
        const data = await response.json();
        
        // Exibir resultados
        divResultados.innerHTML = data.posts.map(post => `
            <div class="resultado">
                <h3>${post.titulo}</h3>
                <p>${post.resumo}</p>
            </div>
        `).join('');
    } catch (error) {
        console.error('Erro na busca:', error);
    }
});
</script>
```

**View:**
```python
def api_buscar(request):
    query = request.GET.get('q', '')
    
    # Simulação - em produção, buscar no banco
    posts = [
        {'titulo': 'Post 1', 'resumo': 'Resumo 1'},
        {'titulo': 'Post 2', 'resumo': 'Resumo 2'},
    ]
    
    # Filtrar posts
    resultados = [p for p in posts if query.lower() in p['titulo'].lower()]
    
    return JsonResponse({'posts': resultados})
```

### 7.2. Like/Unlike sem Recarregar

**Template:**
```html
<button class="btn-like" data-post-id="{{ post.id }}" data-liked="{{ post.curtido }}">
    <i class="far fa-heart"></i>
    <span class="likes-count">{{ post.likes }}</span>
</button>

<script>
document.querySelectorAll('.btn-like').forEach(botao => {
    botao.addEventListener('click', async function() {
        const postId = this.dataset.postId;
        const csrftoken = getCookie('csrftoken');
        
        try {
            const response = await fetch(`/api/posts/${postId}/like/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Content-Type': 'application/json'
                }
            });
            
            const data = await response.json();
            
            // Atualizar UI
            const icon = this.querySelector('i');
            const count = this.querySelector('.likes-count');
            
            if (data.liked) {
                icon.classList.remove('far');
                icon.classList.add('fas');
            } else {
                icon.classList.remove('fas');
                icon.classList.add('far');
            }
            
            count.textContent = data.likes_count;
            
        } catch (error) {
            console.error('Erro:', error);
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
</script>
```

**View:**
```python
import json
from django.http import JsonResponse

def api_like_post(request, post_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
    # Simulação - em produção, trabalhar com banco de dados
    # Verificar se usuário já curtiu
    liked = True  # Toggle
    likes_count = 42  # Contar likes
    
    return JsonResponse({
        'success': True,
        'liked': liked,
        'likes_count': likes_count
    })
```

### 7.3. Carregar Mais Posts (Infinite Scroll)

**Template:**
```html
<div id="posts-container">
    <!-- Posts aqui -->
</div>
<div id="loading" style="display: none;">Carregando...</div>

<script>
let page = 1;
let loading = false;

window.addEventListener('scroll', function() {
    if (loading) return;
    
    const scrollPosition = window.innerHeight + window.scrollY;
    const pageHeight = document.body.offsetHeight;
    
    if (scrollPosition >= pageHeight - 100) {
        carregarMaisPosts();
    }
});

async function carregarMaisPosts() {
    loading = true;
    document.getElementById('loading').style.display = 'block';
    
    try {
        page++;
        const response = await fetch(`/api/posts/?page=${page}`);
        const data = await response.json();
        
        const container = document.getElementById('posts-container');
        
        data.posts.forEach(post => {
            const div = document.createElement('div');
            div.className = 'post-card';
            div.innerHTML = `
                <h3>${post.titulo}</h3>
                <p>${post.resumo}</p>
                <a href="/blog/${post.id}/">Ler mais</a>
            `;
            container.appendChild(div);
        });
        
    } catch (error) {
        console.error('Erro:', error);
    } finally {
        loading = false;
        document.getElementById('loading').style.display = 'none';
    }
}
</script>
```

### 7.4. Formulário AJAX

**Template:**
```html
<form id="form-comentario">
    {% csrf_token %}
    <textarea name="texto" required></textarea>
    <button type="submit">Enviar</button>
</form>

<div id="mensagem"></div>
<div id="comentarios"></div>

<script>
const form = document.getElementById('form-comentario');
const divMensagem = document.getElementById('mensagem');

form.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = new FormData(form);
    const csrftoken = formData.get('csrfmiddlewaretoken');
    const texto = formData.get('texto');
    
    try {
        const response = await fetch('/api/comentarios/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ texto })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Limpar formulário
            form.reset();
            
            // Mostrar mensagem de sucesso
            divMensagem.innerHTML = '<div class="alert alert-success">Comentário enviado!</div>';
            
            // Adicionar comentário à lista
            adicionarComentario(data.comentario);
        }
        
    } catch (error) {
        divMensagem.innerHTML = '<div class="alert alert-danger">Erro ao enviar comentário</div>';
    }
});

function adicionarComentario(comentario) {
    const div = document.createElement('div');
    div.className = 'comentario';
    div.innerHTML = `
        <p><strong>${comentario.autor}</strong> - ${comentario.data}</p>
        <p>${comentario.texto}</p>
    `;
    document.getElementById('comentarios').prepend(div);
}
</script>
```

---

## 8. Bibliotecas JavaScript Úteis

### 8.1. Axios (Alternativa ao Fetch)

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
// GET
axios.get('/api/posts/')
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// POST
axios.post('/api/posts/', {
    titulo: 'Novo Post',
    conteudo: 'Conteúdo'
}, {
    headers: {
        'X-CSRFToken': csrftoken
    }
})
.then(response => console.log(response.data));
</script>
```

### 8.2. Alpine.js (JavaScript Reativo)

```html
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>

<div x-data="{ open: false }">
    <button @click="open = !open">Toggle</button>
    
    <div x-show="open">
        Conteúdo expandido
    </div>
</div>
```

### 8.3. HTMX (Interações sem JavaScript)

```html
<script src="https://unpkg.com/htmx.org@1.9.10"></script>

<button hx-get="/api/posts/" hx-target="#posts">
    Carregar Posts
</button>

<div id="posts"></div>
```

---

## 9. Boas Práticas

### ✅ Faça

```javascript
// Use addEventListener (não onclick inline)
botao.addEventListener('click', function() { ... });

// Use async/await para código mais limpo
async function getData() {
    const response = await fetch('/api/data/');
    return await response.json();
}

// Trate erros
try {
    // código
} catch (error) {
    console.error('Erro:', error);
}

// Use const/let (não var)
const API_URL = '/api/posts/';

// Organize código em funções
function buscarPosts() { ... }
function exibirPosts(posts) { ... }
```

### ❌ Evite

```javascript
// Não use onclick inline
<button onclick="minhaFuncao()">  // RUIM!

// Não esqueça CSRF token em POST
fetch('/api/', { method: 'POST' })  // RUIM!

// Não ignore erros
fetch('/api/').then(r => r.json())  // RUIM! Sem .catch()

// Não use var
var x = 10;  // RUIM! Use const ou let
```

---

## 📝 Exercícios Práticos

### Exercício 1: Busca em Tempo Real

Implemente uma busca que:
1. Busca posts enquanto o usuário digita
2. Mostra resultados sem recarregar a página
3. Debounce (espera usuário parar de digitar)

### Exercício 2: Sistema de Likes

Crie um sistema onde:
1. Usuário pode curtir/descurtir posts
2. Contador atualiza em tempo real
3. Ícone muda de acordo com o estado

### Exercício 3: Comentários AJAX

Implemente:
1. Formulário de comentário
2. Enviar por AJAX
3. Adicionar comentário à lista sem recarregar
4. Validação de campos

---

## 🔗 Recursos Adicionais

- [MDN - Fetch API](https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API)
- [Django + AJAX Tutorial](https://docs.djangoproject.com/en/5.0/topics/serialization/)
- [JavaScript.info](https://javascript.info/)
- [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS)

---

## 📚 Próximos Passos

Após dominar JavaScript com Django, você pode estudar:
- Django REST Framework (APIs completas)
- Django Channels (WebSockets e tempo real)
- Frameworks JavaScript (React, Vue, Angular)
- TypeScript

---

**Parabéns por completar o curso básico de Django!** 🎉
