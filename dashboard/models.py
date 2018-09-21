from django.db import models

# Create your models here.
class mdlSituacao(models.Model):
    descricao = models.CharField('Descricao', max_length=100)

    datacriacao = models.DateTimeField(auto_now_add=True)
    dataalteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'


class mdlOcorrencias(models.Model):
    solicitacao = models.TextField('Solicitação', blank=True)
    situacao = models.ForeignKey('mdlSituacao', on_delete=models.CASCADE, verbose_name='Situação')
    datacriacao = models.DateTimeField(auto_now_add=True)
    dataalteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.situacao

    class Meta:
        verbose_name = 'Ocôrrencia'
        verbose_name_plural = 'Ocôrrencia'