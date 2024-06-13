from django.db import models

# Create your models here.
class Student(models.Model):
    usn=models.CharField(max_length=100)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.

class Customer(models.Model):
    account_no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    aadhar=models.IntegerField(max_length=12)
    pincode=models.IntegerField(max_length=6)

    def _str_(self):
        return self.name
