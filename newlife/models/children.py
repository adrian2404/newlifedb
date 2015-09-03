# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Child(models.Model):
    """Student model"""

    class Meta(object):
        verbose_name=u"Дитина"
        verbose_name_plural= "Дитини" 


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


    birthday = models.DateField(
    blank=False,
    verbose_name=u"Дата народження",
    null=True)


    photo = models.ImageField(
    blank=True,
    verbose_name=u"Фото",
    null=True)


    child_supporter = models.ForeignKey('Supporter',
    verbose_name="Спонсор",
    blank=True,
    null=True,
    on_delete=models.PROTECT)

    problem = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=u"Проблема")
    
    notes = models.TextField(
    blank=True,
    verbose_name=u"Нотатки")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
     