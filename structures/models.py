from django.db import models


class Structure(models.Model):
    region = models.ForeignKey('Region', verbose_name='region')
    country = models.CharField(max_length=64, verbose_name='country')
    value = models.FloatField(verbose_name='value')

    class Meta:
        verbose_name = 'structure'
        verbose_name_plural = 'structures'
        ordering = ['region']

    def __str__(self):
        return self.country


class Region(models.Model):
    title = models.CharField(max_length=64, verbose_name='title')

    class Meta:
        verbose_name = 'region'
        verbose_name_plural = 'regions'
        ordering = ['-title']

    def __str__(self):
        return self.title
