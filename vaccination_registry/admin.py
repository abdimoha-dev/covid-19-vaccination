from django.contrib import admin

from .models import Person,Schedule, SecondVaccination

admin.site.register(Person)
admin.site.register(Schedule)
admin.site.register(SecondVaccination)