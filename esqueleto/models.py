from django.db import models
from django.conf import settings


class Gostos(models.Model):
    gosto = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.gosto}'


class GostosDoPaciente(models.Model):
    nome_do_paciente =  models.CharField(max_length=255)
    gostos = models.ForeignKey(Gostos, on_delete=models.CASCADE)

    #def __str__(self):
       # return f'"{self.text}" - {self.author.username}'

class GostosDoPsico(models.Model):
    nome_do_psico =  models.CharField(max_length=255)
    gostos = models.ForeignKey(Gostos, on_delete=models.CASCADE)

    #def __str__(self):
        #return f'"{self.text}" - {self.author.username}'