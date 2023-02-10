from django.db import models

# Create your models here.

# create company model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    about=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','Non IT'),('Mobile Phones','Mobie Phones')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name + " "+ self.location

class Employee (models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.IntegerField(max_length=10)
    about=models.CharField(max_length=100)
    type=models.TextField()
    position=models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('Software Developer','software developer',),
        ('Project Leader','pl')
    ))

    company=models.ForeignKey(Company,on_delete=models.CASCADE)

