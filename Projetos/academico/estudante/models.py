from django.db import models


class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    curso = models.ForeignKey(
        'curso.Curso', on_delete=models.PROTECT, related_name='estudantes'
    )

    def __str__(self):
        return self.nome
