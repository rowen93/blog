from django.apps import AppConfig
from django.db.models import signals


class UsersConfig(AppConfig):
    name = 'users'

def ready(self)
    import users.signals    