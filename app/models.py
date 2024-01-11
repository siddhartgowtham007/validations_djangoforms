from django.db import models


# Create your models here.


class School(models.Model):
    Sname=models.CharField(max_length=20)
    Sprincipal=models.CharField(max_length=20)
    Slocation=models.CharField(max_length=30)
    Email=models.EmailField('hi@gmail.com')
    Remail=models.EmailField('hi@gmaill.com')
    def __str__(self):
        return self.Sprincipal