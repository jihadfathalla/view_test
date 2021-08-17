from django.shortcuts import render
from doctor.models import Doctor

# Create your views here.



def list_doctors(request):
     doctors = Doctor.objects.all()
     print(doctors)
     pass
