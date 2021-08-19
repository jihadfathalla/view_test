from django.urls import path
from patient import views


app_name= 'patient'

urlpatterns =[
     path('list/patients_informations', views.list_patients_information),
     path('list/patients-orm', views.list_patients_orm , name='list-patients-orm'),
     path('test/procedure/<int:clinic_id_from>/<int:clinic_id_to>/<int:doctor_id_from>/<int:doctor_id_to>/<int:patient_id_from>/<int:patient_id_to>', views.test_procedure),

     path('search/patients-orm/<int:clinic_id_from>/<int:clinic_id_to>/<int:doctor_id_from>/<int:doctor_id_to>/<int:patient_id_from>/<int:patient_id_to>', views.search_patients_orm , name='search-patients-orm'),
     path('search/patients-view/<int:clinic_id_from>/<int:clinic_id_to>/<int:doctor_id_from>/<int:doctor_id_to>/<int:patient_id_from>/<int:patient_id_to>', views.search_patients_view , name='search-patients-orm'),


]