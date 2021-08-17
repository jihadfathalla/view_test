from rest_framework import serializers
from .models import *
from doctor.serializers import DoctorSerializer
from clinic.serializers import ClinicSerializer

class PatientSerializer(serializers.ModelSerializer):
     class Meta:
          model = Patient
          fields = ('id','name' , 'age', 'clinic' ,'clinic_name', 'doctor' , 'doctor_title')
     
     clinic_name = serializers.SerializerMethodField('get_clinics_name')
     doctor_title = serializers.SerializerMethodField('get_doctors_title')

     def get_clinics_name(self, obj):
          return obj.clinic.name

     def get_doctors_title(self, obj):
          return obj.doctor.title