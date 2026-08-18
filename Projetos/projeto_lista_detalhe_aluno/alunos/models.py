from django.db import models

# Create your models here.
class Aluno(models.Model):
   nome = models.CharField(max_length=100)
   idade = models.IntegerField()
   email = models.EmailField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.nome
