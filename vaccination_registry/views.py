from django.shortcuts import render, redirect,HttpResponse,HttpResponsePermanentRedirect
# from .models import Person


from django.contrib.auth.models import User
from django.contrib.auth import login ,authenticate, logout
from django.contrib.auth.decorators import login_required


# home
@login_required(login_url='login')
def home(request):
    return render(request, 'sidebar.html')

# login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'index.html')
            
    else: # Get method -> 
        # check if test user exists
        if User.objects.filter(username='test').exists():
            return render(request, 'accounts/login.html')
        # if test user does not exist, create user
        else:
            user = User.objects.create_user(
                first_name = 'test',
                last_name = 'user',
                username= 'test',
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

