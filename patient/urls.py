from django.urls import path
from patient import views


app_name= 'patient'

urlpatterns =[
<<<<<<< HEAD
     path('list/patients_informations', views.list_patients_information),
     # path('patients_informations/<int:first_clinic_id>/<int:second_clinic_id>/<int:first_doctor_id>/<int:second_doctor_id>/<int:first_patient_id>/<int:second_patient_id>', views.patients_informations),
=======
     path('list/patients_informations', views.list_patients_informations),
     path('list/patients-orm', views.list_patients_orm , name='list-patients-orm'),

>>>>>>> 9a91fc210ae56c9fbf61a149780992529b190772
]