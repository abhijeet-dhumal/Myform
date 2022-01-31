from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import password_validation
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.validators import UnicodeUsernameValidator

# username_validator = UnicodeUsernameValidator()

# class CreateUserForm(UserCreationForm):
#     address=forms.CharField(label='address')
#     image=forms.FileField()
#     first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
#                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
#     last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
#                                widget=(forms.TextInput(attrs={'placeholder': 'First Name'})))
#     email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
#                              widget=(forms.TextInput(attrs={'placeholder': 'First Name'})))
#     password1 = forms.CharField(label=_('Password'),
#                                 widget=(forms.PasswordInput(attrs={'placeholder': 'First Name'})),
#                                 help_text=password_validation.password_validators_help_text_html())
#     password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'placeholder': 'First Name'}),
#                                 help_text=_('Just Enter the same password, for confirmation'))
#     username = forms.CharField(
#         label=_('Username'),
#         max_length=150,
#         help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
#         validators=[username_validator],
#         error_messages={'unique': _("A user with that username already exists.")},
#         widget=forms.TextInput(attrs={'placeholder': 'First Name'})
#     )

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','address','image')

#     def save(self, commit=True):
#         user = super(CreateUserForm, self).save(commit=False)
#         user.first_name = self.cleaned_data["first_name"]
#         user.last_name = self.cleaned_data["last_name"]
#         user.email = self.cleaned_data["email"]
#         user.address = self.cleaned_data["address"]
#         user.image = self.cleaned_data["image"]
#         if commit:
#             user.save()
#         return user

class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role','image','address_line1','city', 'state', 'country','pincode']