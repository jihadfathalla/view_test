from django.urls import path
from doctor import views


app_name= 'doctor'

urlpatterns =[
     path('list/doctors', views.list_doctors),

]