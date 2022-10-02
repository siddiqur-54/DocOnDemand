from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
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