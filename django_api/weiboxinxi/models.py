#-*- coding:utf-8 -*-

from django.db import models

# Create your models here.
class UserBaseInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12, verbose_name='姓名')
    id_card = models.CharField(max_length=18, verbose_name='身份证号')
    telephone = models.CharField(max_length=11, verbose_name='联系方式')
    we_chat = models.CharField(max_length=30, verbose_name='微信')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name.encode('utf-8')