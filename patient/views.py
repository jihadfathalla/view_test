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
def test_procedure(request):
     # cursor = connection.cursor
     # cursor.excute(call 'PatientFullInfoSP()')
     # result = cursor.fetchall()
     # c = connection.cursor()
     # c.execute("BEGIN")
     # c.callproc("PatientFullInfoSP")
     # results = c.fetchall()
     # c.execute("COMMIT")
     # c.close()
     # print (results)
     # return Response(results)

     cursor = connection.cursor()
     try:
          cursor.execute('CALL  PatientFullInfoSP()')
          print("*****************************************",cursor.description)
          result_set = cursor.fetchall()
          print(result_set)
          return Response(result_set)
     finally:
          cursor.close()



             



# def patients_informations(request,first_clinic_id,second_clinic_id, first_doctor_id,second_doctor_id, first_patient_id,second_patient_id):
#      patients_information = PatientInformation.objects.filter(clinic_id__gte=first_clinic_id,clinic_id__lte=second_clinic_id,
#      doctor_id__gte=first_doctor_id,doctor_id__lte=second_doctor_id,
#      id__gte=first_patient_id,id__lte=second_patient_id)
#      print(patients_information)
#      pass

     # print(patients_information)
     # pass

@api_view(['GET', ])
def list_patients_orm(request):
     patients = Patient.objects.all().order_by('id')[:100]
     patient_serializer = PatientSerializer(patients , many=True)
     data = {"response id": '0' ,"data": patient_serializer.data}
     return Response(data)
