# coding:utf-8
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class SearchWords(models.Model):
    word = models.CharField(max_length=80, verbose_name=u'搜索内容')

    class Meta:
        verbose_name = u'搜索关键词'
        verbose_name_plural = verbose_name
