from django.test import TestCase
from .models import Person

class PersonModelTest(TestCase):
    def test_string_representation(self):
        person = Person(first_name = "myname is abdi")
        self.assertEqual(str(person), person.first_name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Person._meta.verbose_name_plural), "persons")
        
        
class HomePageTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/vaccination/home')
        self.assertNotEqual(response.status_code, 404)
        
    def test_index_loads_properly(self):
        response= self.client.get('http://127.0.0.1:8000/vaccination/home')
        self.assertNotEqual(response.status_code, 404)
    
    
# class ModelTestCase()