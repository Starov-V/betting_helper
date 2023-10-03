from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_username, validate_password

class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[validate_username]
    )
    email = models.EmailField(
        unique=True
    )
    password = models.CharField(
        max_length=50,
        null=True,
        default=None,
        validators=[validate_password]
    )
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
