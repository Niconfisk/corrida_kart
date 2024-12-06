from django.db import models
from django.urls import reverse

# Create your models here.

class Piloto(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    equipe = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('piloto-detalhes', args=[str(self.id)])


class Corrida(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    pilotos = models.ManyToManyField(Piloto, related_name="corridas")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('corrida-detalhes', args=[str(self.id)])
