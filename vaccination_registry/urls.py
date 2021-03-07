from django.urls import path

from . import views

urlpatterns = [
    # path('', views.test, name='index'),
    # path('testuser', views.create_test_user, name ='create_test_user'),
    path('login', views.user_login, name='login'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('add_person', views.add_person, name='add_person'),
    path('edit_person/<str:pk>', views.edit_person, name='edit_person'),
    path('all', views.all_vaccinated_persons, name='all'),
    path('delete_person/<str:person_id>',
         views.delete_person, name='delete_person'),
    path('search/', views.search_persons, name='search'),
    path('secondvaccination/<str:user_id>',
         views.second_vaccination, name='secondvaccination'),
    path('relatedvaccinations',
         views.attended_first_second_vaccination, name='related'),
    path('view_person/<str:user_id>', views.view_person, name='view_person'),
    path('small_stats', views.small_stats, name='small_stats'),


    # REST FRAMEWORK APIs
    path('api/', views.apiOverView, name='api-overview'),
    path('api/vaccinated-list/', views.vaccinatedList, name='vaccinated-list'),
    path('api/person-details/<str:pk>/', views.personDetails, name='person-details'),
    path('api/create-person/', views.personCreate, name='create-person'),
    path('api/update-person/<str:pk>/', views.updatePerson, name='update-person'),
    path('api/delete-person/<str:pk>/', views.personDelete, name='delete-person')
]
