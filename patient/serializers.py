from rest_framework import serializers
from rest_framework import fields
from .models import *
from datetime import date, time
from django.db.models import Q
from django.db import models
from rest_framework.fields import CurrentUserDefault
from rest_framework.exceptions import APIException
from django.utils.encoding import force_text
from rest_framework import status
from patient.models import PatientInformation
from .models import *
from doctor.serializers import DoctorSerializer
from clinic.serializers import ClinicSerializer


from doctor.serializers import DoctorSerializer
from clinic.serializers import ClinicSerializer


class PatientInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInformation
        fields = '__all__'



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
