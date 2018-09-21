from django.contrib.auth.backends import ModelBackend as BaseModelBackend

from .models import User

#esse modelo verifica se o usuario existe pelo username caso nao exista ele tenta verificar se existe
#o email como usuario.
class ModelBackend(BaseModelBackend):
    def authenticate(self, username=None, password=None):
        if not username is None:
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass