from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from patient.serializers import PatientInformationSerializer
from patient.models import PatientInformation
from patient.models import Patient ,PatientInformation
from patient.serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from django.db import connection



@api_view(['GET', ])
def list_patients_information(request): 
     patients_information = PatientInformation.objects.all().order_by('id')[:100]
     serializer = PatientInformationSerializer(patients_information, many=True)
     data = {"success": True, "data": serializer.data}
     return Response(data)

@api_view(['GET', ])
def test_procedure(request, clinic_id_from ,clinic_id_to , doctor_id_from , doctor_id_to , patient_id_from, patient_id_to):
     cursor = connection.cursor()
     try:
          # cursor.execute('select * from some_function_2(%s,%s,%s,%s,%s,%s)',(clinic_id_from ,clinic_id_to , doctor_id_from , doctor_id_to , patient_id_from, patient_id_to))
          cursor.execute('select * from get_film()')
          result_set = cursor.fetchall()
          return Response(result_set)
     finally:
          cursor.close()



             



@api_view(['GET', ])
def search_patients_view(request , clinic_id_from ,clinic_id_to , doctor_id_from , doctor_id_to , patient_id_from, patient_id_to):
     
     patients = PatientInformation.objects.filter(clinic_id__gte=clinic_id_from ,clinic_id__lte =clinic_id_to ,
      doctor_id__gte=doctor_id_from , doctor_id__lte= doctor_id_to,
      id__gte = patient_id_from ,id__lte = patient_id_to)
      
     patient_serializer = PatientInformationSerializer(patients , many=True)
     data = {"response id": '0' ,"data": patient_serializer.data}
     return Response(data)


@api_view(['GET', ])
def list_patients_orm(request):
     patients = Patient.objects.all()
     patient_serializer = PatientSerializer(patients , many=True)
     data = {"response id": '0' ,"data": patient_serializer.data}
     return Response(data)


@api_view(['GET', ])
def search_patients_orm(request , clinic_id_from ,clinic_id_to , doctor_id_from , doctor_id_to , patient_id_from, patient_id_to):
     
     patients = Patient.objects.filter(clinic__gte=clinic_id_from ,clinic__lte =clinic_id_to ,
      doctor__gte=doctor_id_from , doctor__lte= doctor_id_to,
      id__gte = patient_id_from ,id__lte = patient_id_to)
      
     patient_serializer = PatientSerializer(patients , many=True)
     data = {"response id": '0' ,"data": patient_serializer.data}
     return Response(data)
