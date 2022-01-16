from django.db import models

# Create your models here.
class Usuario(models.Model):
    """docstring for Usuario."""

    id_usuario  = models.IntegerField(primary_key=True)

    nome        = models.CharField(max_length=100)
    sobrenome   = models.CharField(max_length=100)
    email       = models.CharField(max_length=100)
    senha       = models.CharField(max_length=200)

    descricao     = models.TextField()
    imagem_perfil = models.CharField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.nome, self.sobrenome)
