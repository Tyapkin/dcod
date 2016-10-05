from django.db import models


class Structure(models.Model):
    region = models.CharField(max_length=64, verbose_name='region')
    country = models.CharField(max_length=64, verbose_name='country')
    value = models.FloatField(verbose_name='value')

    class Meta:
        verbose_name = 'structure'
        verbose_name_plural = 'structures'
        ordering = ['region']

    def __str__(self):
        return self.country
