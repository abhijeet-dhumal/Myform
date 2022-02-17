from time import time, timezone
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

class Blog(models.Model):
    CATEGORY=(
        ('Mental health','Mental health'),
        ('Heart disease','Heart disease'),
        ('Covid-19','Covid-19'),
        ('Immunization','Immunization'),
    )
    CHOICES=(
        ('Save as a draft','Save as a draft'),
        ('Post content as a blog','Post content as a blog'),
    )
    name = models.ForeignKey(Doctor, null=True, on_delete= models.CASCADE)
    title = models.CharField("Title ", max_length=50, blank=True)
    image = models.ImageField("Image ",upload_to='images/doctor/blog/',null=True, blank=True)
    category = models.CharField("Category ", max_length=50,choices=CATEGORY,null=True,blank=True) 
    summary = models.CharField("Summary ", max_length=100, blank=True)
    content = models.TextField("Content ", max_length=100, blank=True)
    # complete = models.CharField("Action",max_length=50,choices=CHOICES,null=True,blank=True)
    draft=models.BooleanField("Draft ",default=False)
    # publish=models.DateField("Publish at date ",null=True,blank=True,auto_now=False,auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        if self.title==None:
            return "ERROR-PATIENT NAME IS NULL"
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, null=True, on_delete= models.CASCADE)
    patient = models.ForeignKey(Patient, null=True, on_delete= models.CASCADE)
    speciality=models.CharField("Required speciality ", max_length=50, blank=True)
#     date_of_appointment=models.DateField("Date of appointment ", max_length=50, blank=True)
    Starttime_of_appointment=models.DateTimeField("Start Date/Time of appointment ",auto_now_add=True, null=True)

    def __str__(self):
        if self.speciality==None:
            return "ERROR-DOCTOR SPECIALTY IS NULL"
        return self.speciality
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
