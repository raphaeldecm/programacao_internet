# Gestão acadêmica — projeto inicial

Base didática para as aulas de Programação para Internet. As telas usam exemplos
fixos no HTML; as views apenas renderizam templates, sem consultar ou alterar o banco.
Os botões de salvar e confirmar exclusão estão desabilitados até a implementação.
Os links usam o identificador fictício `1`, independentemente dos registros do banco.

## Executar

Com Python 3.12 ou superior e um ambiente virtual ativo:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse http://127.0.0.1:8000/. Não é necessário cadastrar dados para navegar nas telas.

## Organização

- `academico/`: configurações e rotas principais.
- `curso/`: modelo, views, URLs e `templates/curso/`.
- `estudante/`: modelo, views, URLs e `templates/estudante/`.
- `templates/`: base compartilhada e página inicial.
- `static/css/bootstrap.min.css`: estilos locais, sem dependência de CDN.

## Modelos entregues

`Curso`: nome e carga horária. `Estudante`: nome, matrícula única, e-mail e curso.
Um curso pode ter vários estudantes; cada estudante pertence a um curso.
A exclusão de um curso com estudantes é protegida por `PROTECT`.
As migrações iniciais estão incluídas. O admin mantém a configuração padrão;
os modelos não estão registrados nele.

## Atividades dos alunos

1. **Listagem:** consultar os modelos, enviar o contexto às telas e substituir
   as linhas fixas por laços de template. Tratar listas vazias e gerar links com
   o identificador de cada registro.
2. **Visualização:** buscar pelo `pk`, responder com 404 quando não existir e
   mostrar o curso do estudante e os estudantes de cada curso.
3. **Cadastro:** criar `forms.py` em cada app com Form ou ModelForm; carregar
   os cursos do banco no campo de relacionamento e salvar apenas após validar POST.
4. **Edição:** reutilizar o formulário com os dados da instância e persistir
   alterações válidas. Habilitar os botões de salvar ao implementar as operações.
5. **Validação:** apresentar erros por campo e erros gerais, preservar os dados
   digitados e validar matrícula única e carga horária maior que zero. O modelo
   aceita zero; essa regra deve ser desenvolvida no formulário.
6. **Exclusão:** buscar o registro real na confirmação, habilitar o botão e excluir
   somente em POST. Tratar a tentativa de excluir curso com estudantes vinculados.
7. **Mensagens:** usar `django.contrib.messages` nas operações e apresentar as
   mensagens em `templates/base.html`. Após sucesso, redirecionar para a listagem.

Os comentários nas views e templates indicam os pontos de trabalho. As telas de
cadastro e edição compartilham o mesmo template; a URL distingue o título.
Os formulários já incluem CSRF. Não há implementação de CRUD nem mensagens de
sucesso simuladas nesta base.
