from __future__ import print_function
from django import contrib
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.db.models import Q
from form.filters import BlogFilter
from form.forms import AppointmentForm, BlogForm, DoctorForm, PatientForm, UserRegisterForm
# create your views here 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import *
from django.contrib.auth.models import Group
from django.http import HttpResponse
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
# for flash message
from .decorators import *
from django.contrib import messages


def home(request):
    context={}
    return render(request,"form/home.html",context)

# import httplib2
# import os

# from apiclient import discovery
# import oauth2client
# from oauth2client import client
# from oauth2client import tools
# from oauth2client import file 

# import datetime

# try:
#     import argparse
#     flags = tools.argparser.parse_args([])
# except ImportError:
#     flags = None

# # If modifying these scopes, delete your previously saved credentials
# # at ~/.credentials/calendar-python-quickstart.json
# SCOPES = 'https://www.googleapis.com/auth/calendar'
# CLIENT_SECRET_FILE = 'C:\\Users\\aksha\\Downloads\\client_secret_web.json'
# APPLICATION_NAME = 'HealthManager'

# def get_credentials():
#     """Gets valid user credentials from storage.

#     If nothing has been stored, or if the stored credentials are invalid,
#     the OAuth2 flow is completed to obtain the new credentials.

#     Returns:
#         Credentials, the obtained credential.
#     """
#     home_dir = os.path.expanduser('~')
#     credential_dir = os.path.join(home_dir, '.credentials')
#     if not os.path.exists(credential_dir):
#         os.makedirs(credential_dir)
#     credential_path = os.path.join(credential_dir,
#                                    'C:\\Users\\aksha\\OneDrive\\Desktop\\myform\\form\\calendar-python-quickstart.json')

#     store = oauth2client.file.Storage(credential_path)
#     credentials = store.get()
#     if not credentials or credentials.invalid:
#         flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
#         flow.user_agent = APPLICATION_NAME
#         if flags:
#             credentials = tools.run_flow(flow, store, flags)
#         else: # Needed only for compatibility with Python 2.6
#             credentials = tools.run(flow, store)
#         print('Storing credentials to ' + credential_path)
#     return credentials

    
# """Shows basic usage of the Google Calendar API.

# Creates a Google Calendar API service object and outputs a list of the next
#     10 events on the user's calendar.
# """

# # Refer to the Python quickstart on how to setup the environment:
# # https://developers.google.com/google-apps/calendar/quickstart/python
# # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# # stored credentials.



# from datetime import datetime, timedelta

# @unauthenticated_user
def DoctorLoginForm(request):
    try:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username , password = password)     
            if user is not None:
                login(request, user)
                return redirect('doctorusernames')
            else:
                return HttpResponse("<h1>Registered email or Password is incorrect !!!</h1>")
              
    except Exception as e:
        print(e)                

    context={}
    return render(request,"form/DoctorLoginForm.html",context)

# @unauthenticated_user
def PatientLoginForm(request):
    try:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username , password = password)     
            if user is not None:
                login(request, user)
                return redirect('patientusernames')
            else:
                return HttpResponse("<h1>Registered email or Password is incorrect !!!</h1>")
              
    except Exception as e:
        print(e)                

    context={}
    return render(request,"form/PatientLoginForm.html",context)

# @unauthenticated_user   
def doctor_registerPage(request):
#     f=open("C:\\Users\\aksha\\OneDrive\\Desktop\\myform\\form\\calendar-python-quickstart.json","r+")
#     f.truncate()
    if request.method=='POST':
        form1 = UserRegisterForm(request.POST)
        doctor_reg_form = DoctorForm(request.POST)
        if form1.is_valid() and doctor_reg_form.is_valid():
            form1.save()
            user = form1.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            profile = Doctor.objects.create(user=user)
            doctor_reg_form = DoctorForm(request.POST,request.FILES,instance=profile)
            doctor_reg_form.full_clean()
            doctor_reg_form.save()
            username = form1.cleaned_data.get('username')

            # to assign group name 
            group=Group.objects.get(name='doctor')
            user.groups.add(group)
            
            messages.success(request, 'Account is created for ' + username)

#             credentials = get_credentials()
#             http = credentials.authorize(httplib2.Http())
#             global service
#             service = discovery.build('calendar', 'v3', http=http)  

            return redirect('DoctorLoginForm')  
    else:
        form1 = UserRegisterForm()
        doctor_reg_form = DoctorForm()           

    context = {}   
    context.update({'form1':form1,'doctor_reg_form':doctor_reg_form}) 
    return render(request, 'form/doctor_registerPage.html',context)


# def create_event(start_time,patient,summary=None,duration=45,description=None,location=None):
#         # matches=list(datefinder.find_dates(start_time))
#         # if len(matches):
#         #     start_time=matches[0]
#     end_time=start_time + timedelta(minutes=duration)
#     timeZone='Asia/Kolkata'
#     event = {
#     'summary': f'Appointment with {patient.name}',
#     'location': 'Pune',
#     'description': description,
#     'start': {
#         'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
#         'timeZone': timeZone,
#     },
#     'end': {
#         'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
#         'timeZone': timeZone,
#     },
#     'recurrence': [
#         'RRULE:FREQ=DAILY;COUNT=2'
#     ],
#     # 'attendees': [
#     #     # {'email': 'abhijeetdhumal652@gmail.com'},
#     #     # {'email':'akshaydhumal652@'}
#     # ],
#     'reminders': {
#         'useDefault': False,
#         'overrides': [
#         {'method': 'email', 'minutes': 24 * 60},
#         {'method': 'popup', 'minutes': 10},
#         ],
#     },
#     }

#     event = service.events().insert(calendarId='primary', body=event).execute()
#     print ('Event created: %s' % (event.get('htmlLink')))

# @unauthenticated_user
def patient_registerPage(request):
    if request.method=='POST':
        form1 = UserRegisterForm(request.POST)
        patient_reg_form = PatientForm(request.POST)
        if form1.is_valid() and patient_reg_form.is_valid():
            form1.save()
            user = form1.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            profile = Patient.objects.create(name=user)
            patient_reg_form = PatientForm(request.POST,request.FILES,instance=profile)
            patient_reg_form.full_clean()
            patient_reg_form.save()
            username = form1.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + username)
            
            # to assign group name 
            group=Group.objects.get(name='patient')
            user.groups.add(group)

            return redirect('PatientLoginForm')        
    else:
        form1 = UserRegisterForm()
        patient_reg_form = PatientForm()

    context = {}   
    context.update({'form1':form1,'patient_reg_form':patient_reg_form}) 
    return render(request, 'form/patient_registerPage.html',context)


# def dashboard(request,pk):
#     userdetails=User.objects.get(id=pk)
#     profiledetails=Profile.objects.get(id=pk)
#     current_user=request.user
#     context={'current_user':current_user,'userdetails':userdetails,'profiledetails':profiledetails}
#     return render(request, 'UserDashboard.html',context) 

@login_required
@allowed_users(allowed_roles=['admin','doctor'])
def doctorusernames(request):
    userdetails=User.objects.all()
    doctordetails=Doctor.objects.all()
    patientdetails=Patient.objects.all()
    current_user = request.user
    
    context={"userdetails":userdetails,"doctordetails":doctordetails,'patientdetails':patientdetails,"current_user":current_user}
    return render(request,"form/doctorusername.html",context)

@login_required
@allowed_users(allowed_roles=['admin','patient'])
def patientusernames(request):
    userdetails=User.objects.all()
    doctordetails=Doctor.objects.all()
    patientdetails=Patient.objects.all()
    current_user = request.user
    
    context={"userdetails":userdetails,"doctordetails":doctordetails,'patientdetails':patientdetails,"current_user":current_user}
    return render(request,"form/patientusername.html",context)

@login_required
@allowed_users(allowed_roles=['admin','doctor'])
def doctor_details(request,pk):
    userdetails=User.objects.get(id=pk)
    doctordetails=Doctor.objects.get(id=pk)
    context={'userdetails':userdetails,"doctordetails":doctordetails}
    return render(request,"form/doctor_userdetails.html",context)

@login_required
@allowed_users(allowed_roles=['admin','patient'])
def patient_details(request,pk):
    userdetails=User.objects.get(id=pk)
    

    patientdetails=Patient.objects.get(id=pk)
    
    context={'userdetails':userdetails,'patientdetails':patientdetails}
    return render(request,"form/patient_userdetails.html",context)

@login_required   
@allowed_users(allowed_roles=['admin','doctor']) 
def updatedoctordetails(request,pk):
    userdetail=User.objects.get(id=pk)
    profiledetail=Doctor.objects.get(id=pk)

    imgs=Doctor.objects.filter(user=profiledetail.user)
    
    registerform=UserRegisterForm(instance=userdetail)
    profileform=DoctorForm(instance=profiledetail)
    if request.method=='POST':
        registerform=UserRegisterForm(request.POST,instance=userdetail)
        profileform=DoctorForm(request.POST,instance=profiledetail)
        if registerform.is_valid() and profileform.is_valid():
            registerform.save()
            profileform.save()
            return redirect('doctorusernames')
        else:
            messages.warning(request,f'Username or Password is incorrect !!! ')


    context={'userdetail':userdetail,'profiledetail':profiledetail,'registerform':registerform,'profileform':profileform,'imgs':imgs}
    return render(request,"form/userdetailsform.html",context)

@login_required    
@allowed_users(allowed_roles=['admin','patient'])
def updatepatientdetails(request,pk):
    userdetail=User.objects.get(id=pk)
    profiledetail=Patient.objects.get(id=pk)

    imgs=Patient.objects.filter(user=profiledetail.user)
    
    registerform=UserRegisterForm(instance=userdetail)
    profileform=PatientForm(instance=profiledetail)
    if request.method=='POST':
        registerform=UserRegisterForm(request.POST,instance=userdetail)
        profileform=PatientForm(request.POST,instance=profiledetail)
        if registerform.is_valid() and profileform.is_valid():
            registerform.save()
            profileform.save()
            return redirect('patientusernames')
        else:
            messages.warning(request,f'Username or Password is incorrect !!! ')


    context={'userdetail':userdetail,'profiledetail':profiledetail,'registerform':registerform,'profileform':profileform,'imgs':imgs}
    return render(request,"form/userdetailsform.html",context)

@login_required
@allowed_users(allowed_roles=['admin','doctor'])
def deletedoctordetails(request,pk):
    userdetails=User.objects.get(id=pk)
    
    if request.method=='POST':
        userdetails.delete()
        return redirect('doctorusernames')

    return render(request,"form/delete.html",{'obj':userdetails})

@login_required
@allowed_users(allowed_roles=['admin','patient'])
def deletepatientdetails(request,pk):
    userdetails=User.objects.get(id=pk)
    
    if request.method=='POST':
        userdetails.delete()
        return redirect('patientusernames')

    return render(request,"form/delete.html",{'obj':userdetails})

@login_required
def logoutuser(request):
    logout(request)
    return redirect('home')

@login_required
@allowed_users(allowed_roles=['admin','doctor','patient'])
def blogs_view(request):
    blogdetail=Blog.objects.filter(draft=False).all()
    myFilter = BlogFilter(request.GET, queryset= blogdetail)
    blogdetail = myFilter.qs
    current_user=request.user
    # imgs=Blog.objects.filter(title=blogdetail.title)

    
    context={'blogdetail':blogdetail,'current_user':current_user,'myfilter':myFilter}
    return render(request,"form/blogs_view.html",context)

@login_required
@allowed_users(allowed_roles=['admin','doctor'])
def blogs_drafts(request):
    blogdetail=Blog.objects.filter(draft=True).all()
    myFilter = BlogFilter(request.GET, queryset= blogdetail)
    blogdetail = myFilter.qs
    current_user=request.user
    # imgs=Blog.objects.filter(title=blogdetail.title)

    
    context={'blogdetail':blogdetail,'current_user':current_user,'myfilter':myFilter}
    return render(request,"form/blogs_drafts.html",context)


@login_required
@allowed_users(allowed_roles=['admin','doctor'])
def blogs_update(request,pk):
    blogdetail=Blog.objects.all()
    blogform=BlogForm(request.POST)
    if request.method=='POST':
        blogform=BlogForm(request.POST)
        if blogform.is_valid():
            action = blogform.cleaned_data.get('complete')
            blogform.save()
            return redirect('usernames')
        else:
            messages.warning(request,f'Username or Password is incorrect !!! ')
    
    context={'blogdetail':blogdetail,'blogform':blogform}
    return render(request,"form/blogs_update.html",context)


# for appointments 
@login_required    
@allowed_users(allowed_roles=['admin','doctor','patient'])
def doctorslist(request):
    userdetails=User.objects.all()
    
    doctordetails=Doctor.objects.all()
    
    context={'userdetails':userdetails,"doctordetails":doctordetails}
    return render(request,"form/doctors_list.html",context)
    
@login_required  
@allowed_users(allowed_roles=['admin','patient'])  
def appointment_form(request):
    current_user=request.user
    appointment_details=AppointmentForm(request.POST)
    if request.method=='POST':
        appointment_details=AppointmentForm(request.POST)
        if appointment_details.is_valid():
            appointment_details.save()
#             start_time=appointment_details.cleaned_data.get('Starttime_of_appointment')
#             end_time=start_time + timedelta(minutes=45)
#             patient=appointment_details.cleaned_data.get('patient')
#             speciality=appointment_details.cleaned_data.get('speciality')
#             print(start_time)
#             create_event(start_time,patient,"Appointment",45,f"Appointment with 'Mr/Ms.{patient.name}' regarding '{speciality}'-required speciality cure.")
            return redirect('appointments') 

    context={'current_user':current_user,"appointment_details":appointment_details}
    return render(request,"form/appointments_form.html",context)

@login_required   
@allowed_users(allowed_roles=['admin','doctor','patient']) 
def appointments(request):
    current_user=request.user
    appointment_details=Appointment.objects.all()

    context={'current_user':current_user,"appointment_details":appointment_details}
    return render(request,"form/appointments.html",context)
    
