from django.urls import path

from . import views

urlpatterns = [
    # path('', views.test, name='index'),
    # path('testuser', views.create_test_user, name ='create_test_user'),
    path('login', views.user_login, name = 'login'), 
    path('logout', views.logout, name='logout'),
    path('home', views.home, name = 'home')
]