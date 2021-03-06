from django.shortcuts import render, redirect, HttpResponse, HttpResponsePermanentRedirect
from .models import Person


from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, Http404


# home
@login_required(login_url='login')
def home(request):
    return render(request, 'sidebar.html')

# login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'index.html')

    else:  # Get method ->
        # check if test user exists
        if User.objects.filter(username='test').exists():
            return render(request, 'accounts/login.html')
        # if test user does not exist, create user
        else:
            user = User.objects.create_user(
                first_name='test',
                last_name='user',
                username='test',
                password='test123',
                email='test@covid.com'
            )
            user.save()
            return render(request, 'accounts/login.html')

# logout
# @login_required(login_url='login')


def user_logout(request):
    logout(request)
    return HttpResponse('user_login')

# create vaccinated user
def add_person(request):
    person_age = 10
    if request.method == 'POST':

        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        age = person_age
        place_of_residence = request.POST.get('placeofresidence')
        phone_number = request.POST.get('phonenumber')
        email = request.POST.get('email')
        occupation = request.POST.get('occupation')
        vaccine_name = request.POST.get('vaccineAdministered')
        comorbidity = request.POST.get('comorbidity')

        person = Person(first_name=first_name,
                        last_name=last_name,
                        gender=gender,
                        dob=dob,
                        age=age,
                        place_of_residence=place_of_residence,
                        phone_number=phone_number,
                        email=email,
                        occupation=occupation,
                        vaccine_name=vaccine_name,
                        comorbidity=comorbidity)
        person.save()

        return render(request, 'index.html')

    else:
        return render(request, 'add_person.html')

  