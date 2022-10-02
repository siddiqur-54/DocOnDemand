from django.db import models
from django.db.models.deletion import CASCADE
from doctor.models import Doctor
from patient.models import Patient

# Create your models here.
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