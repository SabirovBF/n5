from django.db import models
from django.http import HttpResponse
import datetime

class Sot(models.Model):
    name = models.CharField('ФИО', max_length=100)

    class Meta:
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочии'
    def __str__(self) -> str:
        return self.name

class Times(models.Model):
    class Meta:
        verbose_name_plural = datetime.datetime.now()

class Matematic(models.Model):
    name = models.CharField('ФИО', max_length=100)
    class Meta:
        verbose_name = 'Переворот'
        verbose_name_plural = 'Переворот'
    def __str__(self) -> str:
        return self.name[::-1]
