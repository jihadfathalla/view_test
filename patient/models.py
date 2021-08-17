from django.db import models
from doctor.models import Doctor
from clinic.models import Clinic

class Patient(models.Model):
     name = models.CharField(max_length=150)
     age = models.IntegerField()
     clinic_id = models.ForeignKey(Clinic,on_delete=models.CASCADE)
     doctor_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)

     def __str__(self):
         return self.name




class PatientInformation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    PName = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    title= models.CharField(max_length=200)
    age= models.IntegerField()
    clinic_id= models.IntegerField()
    doctor_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'PatientFullInfoView'   
