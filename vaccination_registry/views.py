from django.shortcuts import render
from .models import Person
from django.contrib.auth.models import User

#test view

def test(request):
    return render(request, 'sidebar.html')
