from django.db import models
from django.contrib.auth.models import PermissionsMixin, User, UserManager
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import BaseUserManager, AbstractUser

class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    name = models.CharField("Name", max_length=50, blank=True)
    role = models.CharField("Role", max_length=50,default="Doctor", blank=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='images/doctor/',null=True, blank=True)
    address_line1=city = models.CharField("Address_Line1", max_length=100, blank=True)
    city = models.CharField("City", max_length=50, blank=True)
    state = models.CharField("State", max_length=50, blank=True)
    country = models.CharField("Country", max_length=50, blank=True)
    pincode = models.CharField("Pincode", max_length=50, blank=True)
    def __str__(self):
        if self.name==None:
            return "ERROR-PATIENT NAME IS NULL"
        return self.name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Patient(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    # doctor = models.ForeignKey(Doctor, null=True, on_delete= models.CASCADE)
    name = models.CharField("Name", max_length=50, blank=True)
    role = models.CharField("Role", max_length=50,default="Patient", blank=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='images/patient/',null=True, blank=True)
    address_line1=city = models.CharField("Address_Line1", max_length=100, blank=True)
    city = models.CharField("City", max_length=50, blank=True)
    state = models.CharField("State", max_length=50, blank=True)
    country = models.CharField("Country", max_length=50, blank=True)
    pincode = models.CharField("Pincode", max_length=50, blank=True)
    
    def __str__(self):
        if self.name==None:
            return "ERROR-PATIENT NAME IS NULL"
        return self.name
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)