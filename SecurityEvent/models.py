from django.db import models


# Create your models here.
class Event(models.Model):
    number = models.CharField(max_length=10, verbose_name='事件编号')
    name = models.CharField(max_length=30, verbose_name='名称')
    department = models.ForeignKey('department.Department', verbose_name='所属部门',
                                   help_text='即风险事件的检查部门，非涉及部门')
    control = models.CharField(max_length=1, choices=(('Z', '重点'), ('Y', '一般')), verbose_name='控制要求')
    attribute = models.ForeignKey('SecurityEvent.Event', verbose_name='风险属性')

    class Meta:
        verbose_name = '风险事件'
        ordering = ('-number',)


class EventAttribute(models.Model):
    name = models.CharField(max_length=10, verbose_name='风险属性名称')

    class Meta:
        verbose_name = '风险属性'
