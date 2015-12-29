from django.db import models

# Create your models here.
class WorkPlace(models.Model):
    name = models.CharField(max_length=30,verbose_name='地点名称')
    department = models.ForeignKey('department.Department',verbose_name='部门名称')
