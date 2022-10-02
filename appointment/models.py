from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField

# Create your models here.
class Patient(models.Model):
    contact = models.CharField(max_length=15)
    image = models.FileField(upload_to="patient/images", null=True)
    height = models.CharField(max_length=50,null=True)
    weight = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=15,null=True)
    marital_status = models.CharField(max_length=15,null=True)
    blood_group = models.CharField(max_length=15,null=True)
    birth_date = models.DateField()

    type = models.CharField(max_length=15,null=True)
    user = OneToOneField(User, on_delete=CASCADE,null=True)

    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    image = models.FileField(upload_to="doctor/images", null=True)
    contact = models.CharField(max_length=15)
    gender = models.CharField(max_length=15,null=True)
    medical = models.CharField(max_length=25,null=True)
    position = models.CharField(max_length=25,null=True)
    specialities = models.CharField(max_length=50,null=True)

    status = models.CharField(max_length=25,null=True)

    type = models.CharField(max_length=15,null=True)
    user= models.OneToOneField(User, on_delete=CASCADE,null=True)

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    title = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=200,null=True)
    post_date = models.DateField()
    date = models.DateField()
    time = models.CharField(max_length=200,null=True)
    deadline = models.DateField()
    fee = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=100,null=True)

    doctor= models.ForeignKey(Doctor, on_delete=CASCADE,null=True)
    patient= models.ManyToManyField(Patient)

    def __str__(self):
        return self.title