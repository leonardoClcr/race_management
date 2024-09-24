from django.contrib import admin
from corredores.models import Corredores


class CorredoresAdmin(admin.ModelAdmin):
    list_display = ('nome','idade','peso', 'altura', 'genero')
    search_fields = ('nome', 'genero')

admin.site.register(Corredores, CorredoresAdmin)