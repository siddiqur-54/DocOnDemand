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