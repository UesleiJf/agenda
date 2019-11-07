from django.db import models


class Agenda(models.Model):

    local = models.TextField()
    data = models.DateField()
    horario = models.TimeField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    responsavel = models.TextField()
    contato = models.TextField()
    feito = models.BooleanField(default=False)

    def __str__(self):
        return self.local
