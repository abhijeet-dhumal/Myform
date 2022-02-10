from django.contrib import admin

# Register your models here.
from .models import  Appointment, Blog, Doctor, Patient

# admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Blog)
admin.site.register(Appointment)
