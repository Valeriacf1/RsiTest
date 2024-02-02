from django.db import models
from departments.models import Department
from datetime import datetime

# Create your models here.
class Employee(models.Model):
    employnumber = models.IntegerField()
    name =  models.CharField(max_length=100)
    surnames = models.CharField(max_length=100) 
    birthdate = models.DateField()
    address = models.CharField(max_length=70)
    date_of_entry = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return f"{self.name} {self.surnames} - {self.department}"
    #Calcular dias trabajados;
    def days_of_service(self):
        return (datetime.now().date() - self.date_of_entry).days

