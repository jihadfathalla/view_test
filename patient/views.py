from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import api_view , permission_classes
from patient.serializers import PatientInformationSerializer
from patient.models import PatientInformation
from patient.models import Patient ,PatientInformation
from patient.serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view , parser_classes



@api_view(['GET', ])
def list_patients_information(request): 
     patients_information = PatientInformation.objects.all()
     serializer = PatientInformationSerializer(patients_information, many=True)
     data = {"success": True, "data": serializer.data}
     return Response(data)


             



# def patients_informations(request,first_clinic_id,second_clinic_id, first_doctor_id,second_doctor_id, first_patient_id,second_patient_id):
#      patients_information = PatientInformation.objects.filter(clinic_id__gte=first_clinic_id,clinic_id__lte=second_clinic_id,
#      doctor_id__gte=first_doctor_id,doctor_id__lte=second_doctor_id,
#      id__gte=first_patient_id,id__lte=second_patient_id)
#      print(patients_information)
#      pass

     print(patients_information)
     pass

@api_view(['GET', ])
def list_patients_orm(request):
     patients = Patient.objects.all()
     patient_serializer = PatientSerializer(patients , many=True)
     data = {"response id": '0' ,"data": patient_serializer.data}
     return Response(data)
