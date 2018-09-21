from django.urls import path
from ocorrencias import views


app_name = 'ocorrencias'

urlpatterns = [
    path('', views.vwOcorrencias, name='ListaOcorrencias'),
    path('situacao/', views.vwSituacoes, name='ListaSituacao'),
]
