from django.db import models
from django.utils.translation import gettext as _


class State(models.Model):
    initials = models.CharField(verbose_name=_('initials'), max_length=2)
    
    def __str__(self):
        return f'{self.initials}'


class City(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=128)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return f'{self.name} - {self.state}'
