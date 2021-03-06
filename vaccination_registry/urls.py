from django.urls import path

from . import views

urlpatterns = [
    # path('', views.test, name='index'),
    # path('testuser', views.create_test_user, name ='create_test_user'),
    path('login', views.user_login, name = 'login'), 
    path('logout', views.logout, name='logout'),
    path('home', views.home, name = 'home'),
    path('add_person', views.add_person, name = 'add_person'),
    path('edit/<int:person_id>', views.edit_person, name='edit_person'),
    path('all', views.all_vaccinated_persons, name='all'),

]