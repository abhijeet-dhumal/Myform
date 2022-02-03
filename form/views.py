from django import contrib
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.db.models import Q
from form.forms import DoctorForm, PatientForm, UserRegisterForm
# create your views here 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import *
from django.contrib.auth.models import Group
from django.http import HttpResponse
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
            profile = Patient.objects.create(user=user)
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
    patientdetails=Patient.objects.get(id=pk)
    
    context={'userdetails':userdetails,"doctordetails":doctordetails,'patientdetails':patientdetails}
    return render(request,"form/doctor_userdetails.html",context)

@login_required
def patient_details(request,pk):
    userdetails=User.objects.get(id=pk)
    
    doctordetails=Doctor.objects.get(id=pk)
    patientdetails=Patient.objects.get(id=pk)
    
    context={'userdetails':userdetails,"doctordetails":doctordetails,'patientdetails':patientdetails}
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


def blogs(request):
    context={}
    return render(request,"form/blogs.html",context)

