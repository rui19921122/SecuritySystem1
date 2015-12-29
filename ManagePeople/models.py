from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PersonBase(models.Model):
    '''
    人员基础信息
    '''
    name = models.CharField(max_length=10,verbose_name='')
    sex = models.CharField(max_length=1,verbose_name='',choices=(('M','女'),('F','男')))
    birth_day = models.DateField(verbose_name='',blank=True)
    class Meta:
        abstract = True

class Worker(models.Model):
    '''
    职工信息，记录岗位名称
    '''
    #todo 历任工种职位
    duty = models.ForeignKey('',verbose_name='')

class ManagePerson(models.Model):
    '''
    管理人员信息，添加了账号信息
    '''
    user = models.ForeignKey(User,verbose_name='')
    duty = models.ForeignKey('',verbose_name='')
