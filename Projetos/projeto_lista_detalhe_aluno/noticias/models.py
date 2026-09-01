from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.nome}"