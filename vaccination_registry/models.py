from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Max


import random
from django.utils import timezone

class Person(models.Model):
    user_id = models.CharField(primary_key=True,max_length=100, null=False, default=None, unique=True, blank=False) # editable=False,
    first_name = models.CharField(max_length=50, default="kings")
    last_name = models.CharField(max_length=50, default="kings")
    gender = models.CharField(max_length=100, default="male")
    dob = models.DateField(default=timezone.now)
    age = models.IntegerField(default=16)
    place_of_residence = models.CharField(max_length=50, default='isiolo')
    phone_number = models.CharField(max_length=20, default=190)
    email = models.EmailField(default="kongo@gmail.com")
    occupation = models.CharField(max_length=20,default="kings")
    vaccine_name = models.CharField(max_length=20,default="kings")
    date_of_vaccination = models.DateField(default=timezone.now)
    comorbidity = models.CharField(max_length=50, default="kings")
    
    # generate userIDs
    def save(self, *args, **kwargs):
        if not self.user_id:
            prefix = 'COVIDKENYA{}'
            prev_instances=self.__class__.objects.filter(user_id__contains=prefix)
            if prev_instances.exists():
                last_instance_id = prev_instances.last().user_id[-4:]
                self.user_id = prefix+'{0:04d}'.format(int(last_instance_id)+1)
                
            else:
                self.user_id = prefix+'{0:04d}'.format(1)
        super(Person, self).save(*args, **kwargs)
            
        super().save(*kwargs)


    
class Schedule(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_vaccinated = models.DateField() 
    next_vaccination_date = models.DateField() 
    