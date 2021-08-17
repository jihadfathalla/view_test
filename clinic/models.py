from django.db import models

class Clinic(models.Model):
     name = models.CharField(max_length=150)
     is_active = models.BooleanField(default=False)

     def __str__(self):
         return self.name