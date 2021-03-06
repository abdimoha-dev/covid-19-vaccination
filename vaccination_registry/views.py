from django.shortcuts import render, redirect, HttpResponse, HttpResponsePermanentRedirect
from django.http import HttpResponse, Http404

from .models import Person, Schedule

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta

from .forms import PersonForm


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
        form = PersonForm(request.POST)
        if form.is_valid():

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            age = person_age
            place_of_residence = request.POST.get('place_of_residence')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('email')
            occupation = request.POST.get('occupation')
            vaccine_name = request.POST.get('vaccine_name')
            comorbidity = request.POST.get('comorbidity')
            date_of_vaccination = request.POST.get('date_of_vaccination')

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
                            comorbidity=comorbidity,
                            date_of_vaccination=date_of_vaccination)
            person.save()

            # Get date for next vaccination
            period_btwn_vaccination = timedelta(days=4)
            next_vaccination_date = period_btwn_vaccination + \
                datetime.strptime(date_of_vaccination, '%Y-%m-%d')

            second_vaccination = Schedule(
                user=Person.objects.get(pk=person.user_id),
                date_vaccinated=date_of_vaccination,
                next_vaccination_date= next_vaccination_date
            )
            second_vaccination.save()

            return render(request, 'index.html')

    else:
        form = PersonForm()
        return render(request, 'add_person.html', {'form': form})

# Edit a vaccinated person details


def edit_person(request, person_id):
    if request.method == 'GET':
        person = Person.objects.get(pk=person_id)
        context = {'person': person}
        return render(request, 'edit_person.html', context)

    else:
        person_age = 16
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

        Person.objects.filter(id=person_id).update(first_name=first_name,
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
        return render(request, 'add_person.html')


# fetch all vaccinated person
def all_vaccinated_persons(request):
    persons = Person.objects.all()

    context = {
        'persons': persons,
    }
    return render(request, 'all_persons.html', context)


# delete vaccinated user using ID
def delete_person(request, person_id):
    try:
        person = Person.objects.filter(pk=person_id)
        person.delete()
        return all(request)
    except Person.DoesNotExist:
        raise Http404("person does not exist")
