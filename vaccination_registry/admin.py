from django.contrib import admin

from .models import Person,Schedule

admin.site.register(Person)
admin.site.register(Schedule)