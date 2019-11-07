from django.contrib import admin
from .models import Agenda


class AgendaAdmin(admin.ModelAdmin):
    list_display = ['local', 'data', 'horario', 'valor', 'feito', 'pago']


admin.site.register(Agenda, AgendaAdmin)
