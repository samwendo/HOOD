from django import forms
from .models import *

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['occupants_count', 'admin']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['name']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'neighbourhood_id']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['user', 'neighbourhood_id']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['neighbourhood_id']
