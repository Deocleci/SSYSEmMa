from django.db import models
from datetime import date
import dateutil
from dateutil.relativedelta import *
# Create your models here.

class Employees(models.Model):
    name = models.CharField('Nome', max_length=255)
    email = models.CharField(u'Email ', max_length=255)
    department = models.CharField(u'Department ', max_length=255)
    salary = models.DecimalField(u'Salary', max_digits=9, decimal_places= 2, null=True)
    birth_date = models.DateField('Birth Data')


    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['name','birth_date']

    def __str__(self):
        return  self.name

    def average_age(self):
        average = 0
        employees = Employees.objects.all()
        for employee in employees:
            average += relativedelta(date.today(), employee.birth_date).years
        return average/len(employees)

    def report_salary(self):
        average = 0
        employees = Employees.objects.all()
        for employee in employees:
            average += employee.salary
        return average/len(employees)




