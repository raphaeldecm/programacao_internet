from django.db import models

# Create your models here.
class Aluno(models.Model):

   TIPO_CURSO_CHOICES = (
       ('Técnico', 'Técnico'),
       ('Graduação', 'Graduação'),
       ('Pós-graduação', 'Pós-graduação'),
    )
   nome = models.CharField(max_length=100)
   email = models.EmailField()
   data_nascimento = models.DateField(default=None, blank=True, null=True)
   nome_mae = models.CharField(max_length=200)
   telefone = models.CharField(max_length=20)
   observacoes = models.TextField(blank=True, null=True)
   curso = models.CharField(max_length=100, choices=TIPO_CURSO_CHOICES)
   periodo = models.CharField(max_length=20)

   def __str__(self):
       return self.nome

class Disciplina(models.Model):
   nome = models.CharField(max_length=100)
   codigo = models.CharField(max_length=20)
   professor = models.CharField(max_length=100)

   def __str__(self):
       return self.nome

class Funcionario(models.Model):
   nome = models.CharField(max_length=100, blank=False, null=False)
   sobrenome = models.CharField(max_length=100, blank=True)
   cpf = models.CharField(max_length=14)
   tempo_de_servico = models.IntegerField(
       blank=True, # Adiciona a opção de permitir valores nulos no campo tempo_de_servico
       null=True # Adiciona a opção de permitir valores nulos no campo tempo_de_servico. A diferença entre blank e null é que blank é usado para validação de formulários, enquanto null é usado para o banco de dados. Se você quiser permitir que o campo seja opcional tanto no formulário quanto no banco de dados, você deve usar ambos blank=True e null=True
    )
   remuneracao = models.DecimalField(max_digits=10, decimal_places=2)
   cargo = models.CharField(max_length=100)
   email = models.EmailField()
   telefone = models.CharField(max_length=20)

   def __str__(self):
       return self.nome