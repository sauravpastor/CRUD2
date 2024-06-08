from django.db import models

# Create your models here.
class Employee(models.Model):
    EmployeeName = models.CharField(max_length=50)
    EmployeeSalary = models.IntegerField()
    EmployeeRole = models.CharField(max_length=20)
    EmployeePhone = models.IntegerField()
