from django.db import models

# Create your models here.

class Cliente(models.Model):
	nome = models.CharField(max_length=50)
	sobrenome = models.CharField(max_length=50)
	dataNascimento = models.DateField()

