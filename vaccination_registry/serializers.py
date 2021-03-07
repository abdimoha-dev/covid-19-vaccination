from rest_framework import serializers
from .models import Person, SecondVaccination


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'
        # fields = ['first_name','last_name','gender','dob','age','place_of_residence','phone_number','email','occupation','vaccine_name', 'date_of_vaccination','comorbidity']
