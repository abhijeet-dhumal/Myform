from django.db import models
from django.contrib.auth.models import PermissionsMixin, User, UserManager
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import BaseUserManager, AbstractUser

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.CharField("Doctor/Patient",max_length=20,null=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    address_line1=city = models.CharField("Address_Line1", max_length=100, blank=True)
    city = models.CharField("City", max_length=50, blank=True)
    state = models.CharField("State", max_length=50, blank=True)
    country = models.CharField("Country", max_length=50, blank=True)
    pincode = models.CharField("Pincode", max_length=50, blank=True)
    
    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)