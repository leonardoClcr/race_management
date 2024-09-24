from django.db import models


class Corredores(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    genero = models.CharField(max_length=100)
    peso = models.FloatField()
    altura = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.nome