from django.shortcuts import render
from patient.models import Patient ,PatientInformation

# Create your views here.



def list_patients_informations(request):
     patients_information = PatientInformation.objects.all()
     print(patients_information)
     pass
