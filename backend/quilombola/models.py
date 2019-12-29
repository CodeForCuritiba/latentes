from django.contrib.gis.db import models
from django.utils.translation import gettext as _


class Phase(models.Model):
    phase_no = models.PositiveSmallIntegerField(verbose_name=_('phase number'))
    name = models.CharField(verbose_name=_('name'), max_length=64)

    def __str__(self):
        return f'{self.name}'


class Community(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    area = models.DecimalField(verbose_name=_('area'), max_digits=19, decimal_places=8, blank=True, null=True)
    family_no = models.PositiveIntegerField(verbose_name=_('number of families'), default=0, blank=True, null=True)
    city = models.ForeignKey('base.City', related_name='communities', verbose_name=_('city'), on_delete=models.SET_NULL, null=True, blank=True)

    geometry = models.PolygonField(null=True, blank=False)

    def __str__(self):
        return f'{self.name}'
