from django.urls import path
from patient import views


app_name= 'patient'

urlpatterns =[
     path('list/patients_informations', views.list_patients_informations),
     path('list/patients-orm', views.list_patients_orm , name='list-patients-orm'),

]