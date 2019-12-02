from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Neighbourhood(models.Model):
    image_path = models.ImageField(upload_to = 'images/', null =True, blank = True, default = '../static/images/noimage.svg')
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    description = models.TextField(max_length = 300, blank = True, default = 'No description')
    occupants_count = models.IntegerField(default = '0')
    admin = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def find_neighbourhood(neighbourhood_id):
        neighbourhood = Neighbourhood.objects.get(id = neighbourhood_id)
        return neighbourhood

    def update_neighborhood(self, item, value):
        self.update(item = value)

    def update_occupants(self, value):
        self.update(occupants_count = value)

class User(models.Model):
    profile_picture = models.ImageField(upload_to = 'images/', null =True, blank = True, default = '../static/images/noimage.svg')
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    id_number = models.IntegerField()
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)
    email_address = models.EmailField(max_length=254)
    role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Resident', 'Resident')], default='Resident')

    def __str__(self):
        return self.name.username

class Business(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)
    email_address = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_business(business_id):
        business = Business.objects.get(id = business_id)
        return business

    def update_business(self, item, value):
        self.update(item = value)

    @classmethod
    def search_business(cls, name):
        businesses = cls.objects.filter(name__icontains=name).all()
        return businesses

class Category(models.Model):
    category_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.category_name

class News(models.Model):
    image_path = models.ImageField(upload_to = 'images/', null =True, blank = True, default = '../static/images/noimage.svg')
    title = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.TextField(max_length = 300, blank = True, default = 'No description')
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Service(models.Model):
    image_path = models.ImageField(upload_to = 'images/', null =True, blank = True, default = '../static/images/noimage.svg')
    title = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.TextField(max_length = 300, blank = True, default = 'No description')
    location = models.CharField(max_length = 100)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
