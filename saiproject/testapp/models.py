from django.db import models

# Create your models here.
class School(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=60)
    sclass=models.CharField(max_length=5)
    sadr=models.CharField(max_length=60)
    scl=models.CharField(max_length=30)

class College(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=60)
    sclass=models.CharField(max_length=5)
    sadr=models.CharField(max_length=60)
    college=models.CharField(max_length=30)

class Degree(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=60)
    sclass=models.CharField(max_length=10)
    sadr=models.CharField(max_length=60)
    degree=models.CharField(max_length=30)
