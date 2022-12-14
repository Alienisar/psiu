from django import forms


class GostosdoPacienteForm(forms.Form):
    nome = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
   
    gostos = models.ForeignKey(Gostos, on_delete=models.CASCADE)
    def __str__(self):
        return f'"{self.gostos}" - {self.nome.username}'