from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.user = User(id = 5, username = 'wendo', password = '12345', email = 'wendosam21@gmail.com')
        self.Neighbourhood = Neighbourhood(id = 5, name = 'samhome', admin = self.user, location = 'kangemi')

    def tearDown(self):
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.neighbourhood.save()
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_create_neighbourhood(self):
        self.user.save()
        self.neighbourhood.create_neighbourhood()
        neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods) > 0)

    def test_delete_neighbourhood(self):
        self.user.save()
        self.neighbourhood.create_neighbourhood()
        self.neighbourhood.delete_neighbourhood()
        neighbourhoods = Neighbourhood.objects.all()
        self.assertEqual(len(neighbourhoods), 0)

    def test_find_neighbourhood(self):
        self.user.save()
        self.neighbourhood.create_neighbourhood()
        neighbourhood = Neighbourhood.find_neighbourhood(5)
        self.assertEqual(len(neighbourhoods), 1)

    def test_update_neighborhood(self):
        self.user.save()
        self.neighbourhood.create_neighbourhood()
        self.neighbourhood.update_neighbourhood(occupants_count = 50)
        self.assertEqual(self.neighbourhood.occupants_count, 50)

    def test_update_occupants(self):
        self.user.save()
        self.neighbourhood.create_neighbourhood()
        self.neighbourhood.update_occupants(50)
        self.assertEqual(self.neighbourhood.occupants_count, 50)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.user = User(id = 5, username = 'wendo', password = '12345', email = 'wendosam21@gmail.com')
        self.Neighbourhood = Neighbourhood(id = 5, name = 'samsville', admin = self.user, location = 'moringa')
        self.business = User(id = 5, name = 'airtel', user = self.user, neighbourhood_id = self.neighbourhood,  email_address = 'photolee@gmail.com')

    def tearDown(self):
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()
        Business.objects.all().delete()

    def test_instance(self):
        self.business.save()
        self.assertTrue(isinstance(self.business,Business))

    def test_create_business(self):
        self.user.save()
        self.neighbourhood.save()
        self.business.create_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_business(self):
        self.user.save()
        self.neighbourhood.save()
        self.business.create_business()
        self.business.delete_business()
        businesses = Business.objects.all()
        self.assertEqual(len(businesses), 0)

    def test_find_business(self):
        self.user.save()
        self.neighbourhood.save()
        self.business.create_business()
        business = Business.find_business(5)
        self.assertEqual(len(business), 1)

    def test_update_business(self, item, value):
        self.user.save()
        self.neighbourhood.save()
        self.business.create_business()
        self.business.update_business(email_address = 'hf@gmail.com')
        self.assertEqual(self.business.email_address, 'hf@gmail.com')

    def test_search_business(cls, name):
        self.user.save()
        self.neighbourhood.save()
        self.business.create_business()
        business = Business.search_business('airtel')
        self.assertEqual(len(business), 1)

