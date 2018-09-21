from django.shortcuts import render
from dashboard.models import mdlSituacao, mdlOcorrencias
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def vwOcorrencias(request):
    context = {
        'pgOcorrencias': 'active',
        'Ocorrencias': mdlOcorrencias.objects.all()
    }
    return render(request, 'ocorrencias/ocorrencias.html', context)


@login_required()
def vwSituacoes(request):
    context = {
        'pgSituacoes': 'active',
        'cad_situacao': mdlSituacao.objects.all()
    }
    return render(request, 'ocorrencias/cad_status.html', context)