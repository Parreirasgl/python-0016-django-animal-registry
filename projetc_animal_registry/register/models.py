from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    código = models.CharField(max_length=200)
    historico = models.TextField()

