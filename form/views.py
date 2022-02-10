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
from . import signals
# for flash message
from .decorators import *
from django.contrib import messages

def LoginForm(request):
    try:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username , password = password)     
            if user is not None:
                login(request, user)
                return redirect('usernames')
            else:
                return HttpResponse("<h1>Registered email or Password is incorrect !!!</h1>")
              
    except Exception as e:
        print(e)                

    context={}
    return render(request,"form/LoginForm.html",context)
    
def doctor_registerPage(request):
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
            messages.success(request, 'Account is created for ' + username)

            return redirect('LoginForm')    
    else:
        form1 = UserRegisterForm()
        doctor_reg_form = DoctorForm()           

    context = {}   
    context.update({'form1':form1,'doctor_reg_form':doctor_reg_form}) 
    return render(request, 'form/doctor_registerPage.html',context)

def patient_registerPage(request):
    if request.method=='POST':
        form1 = UserRegisterForm(request.POST)
        patient_reg_form = PatientForm(request.POST)
        if form1.is_valid() and patient_reg_form.is_valid():
            form1.save()
            user = form1.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            profile = Patient.objects.create(name=user.name)
            patient_reg_form = PatientForm(request.POST,request.FILES,instance=profile)
            patient_reg_form.full_clean()
            patient_reg_form.save()
            username = form1.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + username)

            return redirect('LoginForm')        
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
def usernames(request):
    userdetails=User.objects.all()
    doctordetails=Doctor.objects.all()
    patientdetails=Patient.objects.all()
    current_user = request.user
    print(f"current:{current_user.id}")
    
    context={"userdetails":userdetails,"doctordetails":doctordetails,'patientdetails':patientdetails,"current_user":current_user}
    return render(request,"form/username.html",context)

@login_required
def doctor_details(request,pk):
    userdetails=User.objects.get(id=pk)
    
    doctordetails=Doctor.objects.get(id=pk)
    
    context={'userdetails':userdetails,"doctordetails":doctordetails}
    return render(request,"form/doctor_userdetails.html",context)

@login_required
def patient_details(request,pk):
    userdetails=User.objects.get(id=pk)
    

    patientdetails=Patient.objects.get(id=pk)
    
    context={'userdetails':userdetails,'patientdetails':patientdetails}
    return render(request,"form/patient_userdetails.html",context)

@login_required    
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
            return redirect('usernames')
        else:
            messages.warning(request,f'Username or Password is incorrect !!! ')


    context={'userdetail':userdetail,'profiledetail':profiledetail,'registerform':registerform,'profileform':profileform,'imgs':imgs}
    return render(request,"form/userdetailsform.html",context)

@login_required    
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
            return redirect('usernames')
        else:
            messages.warning(request,f'Username or Password is incorrect !!! ')


    context={'userdetail':userdetail,'profiledetail':profiledetail,'registerform':registerform,'profileform':profileform,'imgs':imgs}
    return render(request,"form/userdetailsform.html",context)

@login_required
def deletedoctordetails(request,pk):
    userdetails=User.objects.get(id=pk)
    
    if request.method=='POST':
        userdetails.delete()
        return redirect('usernames')

    return render(request,"form/delete.html",{'obj':userdetails})

@login_required
def deletepatientdetails(request,pk):
    userdetails=User.objects.get(id=pk)
    
    if request.method=='POST':
        userdetails.delete()
        return redirect('usernames')

    return render(request,"form/delete.html",{'obj':userdetails})

@login_required
def logoutuser(request):
    logout(request)
    return redirect('LoginForm')

@login_required
def blogs_view(request):
    blogdetail=Blog.objects.filter(draft=False).all()
    myFilter = BlogFilter(request.GET, queryset= blogdetail)
    blogdetail = myFilter.qs
    current_user=request.user
    # imgs=Blog.objects.filter(title=blogdetail.title)

    
    context={'blogdetail':blogdetail,'current_user':current_user,'myfilter':myFilter}
    return render(request,"form/blogs_view.html",context)

@login_required
def blogs_drafts(request):
    blogdetail=Blog.objects.filter(draft=True).all()
    myFilter = BlogFilter(request.GET, queryset= blogdetail)
    blogdetail = myFilter.qs
    current_user=request.user
    # imgs=Blog.objects.filter(title=blogdetail.title)

    
    context={'blogdetail':blogdetail,'current_user':current_user,'myfilter':myFilter}
    return render(request,"form/blogs_drafts.html",context)


@login_required
def blogs_update(request,pk):
    blogdetail=Blog.objects.all()
    blogform=BlogForm(request.POST)
    if request.method=='POST':
        blogform=BlogForm(request.POST)
        if blogform.is_valid():
            action = blogform.cleaned_data.get('complete')
            blogform.save()
            # if action=='Post content as a blog':
            # else:
            #     seconds = Blog.objects.all()
            #     for second in seconds:
            #         for i in second.objects.filter(link_field=second):
            #             print(i.id)
            #     blog_content = blogform.cleaned_data.get('content')
            #     blog_id=blogform.cleaned_data.get('id')
            #     print("id: ",blog_id)
            #     pass
            return redirect('usernames')
        else:
            messages.warning(request,f'Username or Password is incorrect !!! ')
    
    context={'blogdetail':blogdetail,'blogform':blogform}
    return render(request,"form/blogs_update.html",context)


# for appointments 
@login_required    
def doctorslist(request):
    userdetails=User.objects.all()
    
    doctordetails=Doctor.objects.all()
    
    context={'userdetails':userdetails,"doctordetails":doctordetails}
    return render(request,"form/doctors_list.html",context)

@login_required    
def appointment_form(request):
    # for calendar api 
    '''
    clientID: 1047607298468-j2qspk4pbibggrg1bp4h9nen2c7lofu1.apps.googleusercontent.com
    clientsecret: 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
    '''
    from apiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    scopes=['https://www.googleapis.com/auth/calendar']
    flow=InstalledAppFlow.from_client_secrets_file("C:\\Users\\aksha\\Downloads\\client_secret_tv.json",scopes=scopes)
    '''get credentials for user '''
    # credentials=flow.run_console()
    # pickle.dump(credentials,open("C:\\Users\\aksha\\OneDrive\\Desktop\\myform\\form\\token.pkl","wb"))
    import pickle
    credentials=pickle.load(open("C:\\Users\\aksha\\OneDrive\\Desktop\\myform\\form\\token.pkl","rb"))
    # credentials=open("C:\\Users\\aksha\\OneDrive\\Desktop\\myform\\form\\token.pkl","rb")
    # print(creden)
    service=build("calendar","v3",credentials=credentials)
    result=service.calendarList().list().execute()
    # print(result['items'][0])

    '''Get event '''
    calendar_id=result['items'][0]['id']
    result=service.events().list(calendarId=calendar_id).execute()
    # print(result['items'][0])

    '''create an event'''
    # Refer to the Python quickstart on how to setup the environment:
    # https://developers.google.com/calendar/quickstart/python
    # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
    # stored credentials.

    from datetime import datetime, timedelta
    def create_event(start_time, summary=None,duration=45,description=None,location=None):
        # matches=list(datefinder.find_dates(start_time))
        # if len(matches):
        #     start_time=matches[0]
        end_time=start_time + timedelta(minutes=duration)
        timeZone='Asia/Kolkata'
        event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timeZone,
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timeZone,
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }
        return service.events().insert(calendarId=calendar_id,body=event).execute()

    current_user=request.user
    appointment_details=AppointmentForm(request.POST)
    if request.method=='POST':
        appointment_details=AppointmentForm(request.POST)
        if appointment_details.is_valid():
            appointment_details.save()
            start_time=appointment_details.cleaned_data.get('Starttime_of_appointment')
            end_time=start_time + timedelta(minutes=45)
            doctor=appointment_details.cleaned_data.get('doctor')
            speciality=appointment_details.cleaned_data.get('speciality')
            print(start_time)
            create_event(start_time,"Appointment",45,f"Appointment with 'Dr.{doctor.name}' regarding '{speciality}'-required speciality cure.")
            return redirect('appointments') 

    context={'current_user':current_user,"appointment_details":appointment_details}
    return render(request,"form/appointments_form.html",context)

@login_required    
def appointments(request):
    current_user=request.user
    appointment_details=Appointment.objects.all()

    context={'current_user':current_user,"appointment_details":appointment_details}
    return render(request,"form/appointments.html",context)
    