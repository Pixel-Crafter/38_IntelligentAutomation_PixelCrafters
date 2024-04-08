from django.db import models

class Employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    experience = models.IntegerField()
    previous_company = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=200)
    status = models.CharField(max_length=20)