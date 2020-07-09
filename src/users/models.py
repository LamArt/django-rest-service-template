from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models


class User(AbstractUser):
    """Specific user-related data. Handles auth"""
    middle_name = models.CharField(verbose_name=_('Middle name'), max_length=256)

    def get_full_name(self) -> str:
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    def __str__(self) -> str:
        return self.username + ' ' + self.first_name + ' ' + self.last_name


class Profile(models.Model):
    """Business-logic specific information about users. Handle business logic"""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)