from rest_framework import serializers
from rest_framework import fields
from .models import *
from datetime import date, time
from django.db.models import Q
from django.db import models
from rest_framework.fields import CurrentUserDefault
from rest_framework.exceptions import APIException
from django.utils.encoding import force_text
from rest_framework import status
from patient.models import PatientInformation


class PatientInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInformation
        fields = '__all__'
