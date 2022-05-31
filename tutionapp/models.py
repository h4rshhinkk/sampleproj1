from decimal import Clamped
from email.headerregistry import Address
from django.db import models

# Create your models here. 

class UserRegistration(models.Model):
    StudentImage=models.ImageField(upload_to='Student_Images/',blank='true',null='true')
    StudentName=models.CharField(max_length=50)
    ParentName=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Board=models.CharField(max_length=50)
    StudentClass=models.CharField(max_length=50)
    SchoolName=models.CharField(max_length=50)
    Address=models.CharField(max_length=100)
    StudentEmail=models.CharField(max_length=30)
    StudentPhone=models.CharField(max_length=50)
    ParentPhone=models.CharField(max_length=50)
    StudentPassword=models.CharField(max_length=50)
   
    # Status=models.CharField(max_length=50)



class Contactus(models.Model):
    ReqName=models.CharField(max_length=50)
    ReqEmail=models.CharField(max_length=50)
    ReqMobile=models.CharField(max_length=50)
    ReqMessage=models.CharField(max_length=500)


class TeacherRegistration(models.Model):
    TeacherName=models.CharField(max_length=30)
    TeacherBoard=models.CharField(max_length=50)
    TeacherClass=models.CharField(max_length=50)
    TeacherSubject=models.CharField(max_length=50)
    TeacherPlace=models.CharField(max_length=50)
    TeacherPhone=models.CharField(max_length=50)
    TeacherEmail=models.CharField(max_length=50)
    TeacherPassword=models.CharField(max_length=50) 
