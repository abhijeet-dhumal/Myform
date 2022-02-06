from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Blog, Doctor, Patient
from django.contrib.auth import password_validation

class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name','role','phone','image','address_line1','city', 'state', 'country','pincode']

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','role','phone','image','address_line1','city', 'state', 'country','pincode']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

