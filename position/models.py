from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class ManagePosition(models.Model):
    name = models.CharField(max_length=20,verbose_name='岗位名称')
    duty = models.ManyToManyField('',verbose_name='工作职责')
    department = models.ForeignKey('department.Department',verbose_name='部门名称')
    requirement = models.ManyToManyField('',verbose_name='量化要求')
    leader = models.ForeignKey('self',verbose_name='直接领导')
    standard = models.ManyToManyField('',verbose_name='岗位标准')
    def save(self,*args,**kwargs):
        '''
        存储前确认，确保直接领导不为自己
        :param args:
        :param kwargs:
        :return:
        '''
        if self.leader_pk == self.pk:
            raise ValidationError("直接领导不能为自己")
        else:
            super(ManagePosition, self).save(*args,**kwargs)

class WorkerPosition(models.Model):
    name = models.CharField(max_length=30,verbose_name='岗位名称',help_text='岗位名称应尽可能详细，如直通场车间二号助理值班员（外勤）')
    department = models.ForeignKey('department.Department',verbose_name='部门名称')
    place = models.ManyToManyField('',verbose_name='工作地点')
    attribute = models.ForeignKey('position.WorkerPositionAttribute',verbose_name='岗位类型')
    class Meta:
        verbose_name='职工工作岗位'

class WorkerPositionAttribute(models.Model):
    name = models.CharField(max_length=20,verbose_name='类型名称')
    system = models.ForeignKey('position.WorkerSystem',verbose_name='专业系统')
    class Meta:
        verbose_name='岗位类型'

class WorkerSystem(models.Model):
    name = models.CharField(max_length=20,verbose_name='专业系统名称',help_text='如接发列车等')
    class Meta:
        verbose_name='专业系统名称'
