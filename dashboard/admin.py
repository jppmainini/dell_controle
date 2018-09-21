from django.contrib import admin
from .models import mdlSituacao, mdlOcorrencias

# Register your models here.
class adminSituacao(admin.ModelAdmin):
    list_display = ['id', 'descricao', 'datacriacao']

class adminOcorrencias(admin.ModelAdmin):
    list_display = ['id', 'datacriacao', 'situacao']


admin.site.register(mdlSituacao, adminSituacao)
admin.site.register(mdlOcorrencias, adminOcorrencias)