from django.db import models


class Agenda(models.Model):

    local = models.TextField()
    data = models.DateField()
    horario = models.TimeField()
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    responsavel = models.TextField(null=True, blank=True)
    contato = models.TextField(null=True, blank=True)
    feito = models.BooleanField(default=False)
    pago = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Agenda Projeto Cordas'
        verbose_name_plural = 'Agenda Projeto Cordas'
        unique_together = ('data', 'horario')
        ordering = ['data', 'horario']

    def __str__(self):
        return self.local
