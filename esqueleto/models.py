#from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Gostos(models.Model):
    gosto = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.gosto}'



class GostosDoPaciente(models.Model):
    nome_do_paciente =  models.CharField(max_length=255)
    gostos = models.ForeignKey(Gostos, on_delete=models.CASCADE)

    def __str__(self):
       return f'"{self.gostos}" - {self.nome_do_paciente}'

class GostosDoPsico(models.Model):
    nome_do_psico =  models.CharField(max_length=255)
    gostos = models.ForeignKey(Gostos, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.gostos}" - {self.nome_do_psico}'

#class User(AbstractUser):
    #is_paciente = models.BooleanField(default=False)
    #is_psico = models.BooleanField(default=False)

#class Paciente(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    #interests = models.ManyToManyField(Subject, related_name='interested_students')