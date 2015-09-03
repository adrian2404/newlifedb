# -*- coding: utf-8 -*-
from django.db import models

class Supporter(models.Model):
    """Group model"""

    class Meta(object):
        verbose_name=u"Спонсор"
        verbose_name_plural= "Спонсори"



    first_name = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=u"Ім'я")


    last_name = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=u"Прізвище")


    middle_name = models.CharField(
    max_length=256,
    blank=True, 
    verbose_name=u"По-батькові",
    default='')


    photo = models.ImageField(
    blank=True,
    verbose_name=u"Фото",
    null=True)

    country = models.CharField(
    max_length=256,
    blank=True, 
    verbose_name=u"Країна",
    default='')

    child_supporting = models.ForeignKey('Child',
    verbose_name="Підтримує",
    blank=False,
    null=True,
    on_delete=models.PROTECT)
    
    notes = models.TextField(
    blank=True,
    verbose_name=u"Нотатки")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)