from django.contrib import admin

from .models import Gostos, GostosDoPaciente, GostosDoPsico

admin.site.register(Gostos)
admin.site.register(GostosDoPaciente)
admin.site.register(GostosDoPsico)