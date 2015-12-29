from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=15,verbose_name='')
    attribute = models.CharField(max_length=1,choices=(('J','机关'),('C','车间')))
