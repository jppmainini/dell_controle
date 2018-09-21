import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


# Create your models here.
#Tabela usuarios compativel com o django
class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Apelido / Usuário', max_length=30, unique=True, validators=[
        validators.RegexValidator(regex=('^[\w.@+-]+$'),message=(
            'Informe um nome de usuário válido. '
            'Este valor deve conter apenas letras e numeros '
            'os caracteres: @/./+/- .', 'invalid'
        ))
    ], help_text='Um nome curto que será usado para identificá-lo de forma unica na plataforma '
    )
    '''
    username = models.CharField('Apelido / Usuário', max_length=30, unique=True, validators=[
        validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'Informe um nome de usuário válido. '
            'Este valor deve conter apenas letras e numeros '
            'os caracteres: @/./+/- .', 'invalid'
        )
    ], help_text='Um nome curto que será usado para identificá-lo de forma unica na plataforma '
    )
    '''
    name = models.CharField('Nome', max_length=150)
    email = models.EmailField('Email', unique=True)
    is_active = models.BooleanField('Ativo', default=True)
    is_staff = models.BooleanField('Equipe', default=False)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    object = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]