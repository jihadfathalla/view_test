from django.shortcuts import render
from patient.models import Patient ,PatientInformation
from patient.serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view , parser_classes

# Create your views here.



def list_patients_informations(request):
     patients_information = PatientInformation.objects.all()
     print(patients_information)
     pass

@api_view(['GET', ])
def list_patients_orm(request):
     patients = Patient.objects.all().order_by('id')[:100]
     patient_serializer = PatientSerializer(patients , many=True)
     data = {"response id": '0' ,"data": patient_serializer.data}
     return Response(data)