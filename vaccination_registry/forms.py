from django import forms


GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
VACCINE_CHOICES = (('AstraZeneca', 'AstraZeneca'),
                   ('Moderna', 'Moderna'), ('Pfizer', 'Pfizer'))
COMORBIDITY_CHOICES = (('None','None'), ('TB','TB'),('HIV','HIV'))


class DateInput(forms.DateInput):
    input_type = 'date'

from django.core.files.uploadedfile import SimpleUploadedFile
class PersonForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    gender = forms.CharField(
        label='Gender', widget=forms.RadioSelect(choices=GENDER_CHOICES))
    dob = forms.DateField(widget=DateInput)
    place_of_residence = forms.CharField(label='First Name', max_length=50)
    phone_number = forms.CharField()
    email = forms.EmailField(label='Email')
    occupation = forms.CharField(label='Occupation')
    vaccine_name = forms.CharField(
        label='Vaccine Name', widget=forms.RadioSelect(choices=VACCINE_CHOICES))
    comorbidity = forms.CharField(label='Comorbidity')
    date_of_vaccination = forms.DateField(
        label='Date Of Vaccination', widget=DateInput)


class SecondVaccinationForm(forms.Form):
    
    date_of_second_vaccination = forms.DateField(
        label='Date Of second Vaccination', widget=DateInput)
    effects = forms.CharField(label='Second Vaccination', max_length=50)
