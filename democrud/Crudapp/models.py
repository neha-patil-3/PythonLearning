from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=30)
    emp_code = models.CharField(max_length=3)
    mobile_number = models.CharField(max_length=10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
