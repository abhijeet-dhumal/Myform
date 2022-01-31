from django import contrib
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.db.models import Q
from form.forms import ProfileRegisterForm, UserRegisterForm
# create your views here 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import *
from django.contrib.auth.models import Group
from .models import Profile
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
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        p_reg_form = ProfileRegisterForm(request.POST)
        if form.is_valid() and p_reg_form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            profile = Profile.objects.create(user=user)
            p_reg_form = ProfileRegisterForm(request.POST,request.FILES,instance=profile)
            p_reg_form.full_clean()
            p_reg_form.save()
            messages.success(request, f'Your account has been sent for approval!')
            return redirect('LoginForm')
    else:
        form = UserRegisterForm()
        p_reg_form = ProfileRegisterForm()
    context = {
        'registerform': form,
        'profileform': p_reg_form
    }
    return render(request, 'form/SignUpForm.html', context)

def dashboard(request,pk):
    userdetails=User.objects.get(id=pk)
    profiledetails=Profile.objects.get(id=pk)
    current_user=request.user
    context={'current_user':current_user,'userdetails':userdetails,'profiledetails':profiledetails}
    return render(request, 'UserDashboard.html',context) 

@login_required
def usernames(request):
    userdetails=User.objects.all()
    profiledetails=Profile.objects.all()
    current_user = request.user
    print(f"current:{current_user.id}")
    
    context={"userdetails":userdetails,"profiledetails":profiledetails,"current_user":current_user}
    return render(request,"form/username.html",context)

@login_required
def UserDetails(request,pk):
    userdetails=User.objects.get(id=pk)
    
    profiledetails=Profile.objects.get(id=pk)
    
    context={'userdetails':userdetails,"profiledetails":profiledetails}
    return render(request,"form/userdetails.html",context)

@login_required    
def updateUserdetails(request,pk):
    userdetail=User.objects.get(id=pk)
    profiledetail=Profile.objects.get(id=pk)

    imgs=Profile.objects.filter(user=profiledetail.user)
    
    registerform=UserRegisterForm(instance=userdetail)
    profileform=ProfileRegisterForm(instance=profiledetail)
    if request.method=='POST':
        registerform=UserRegisterForm(request.POST,instance=userdetail)
        profileform=ProfileRegisterForm(request.POST,instance=profiledetail)
        if registerform.is_valid() and profileform.is_valid():
            registerform.save()
            profileform.save()
            return redirect('usernames')
        else:
            messages.warning(request,f'Username or Password is incorrect !!! ')


    context={'userdetail':userdetail,'profiledetail':profiledetail,'registerform':registerform,'profileform':profileform,'imgs':imgs}
    return render(request,"form/userdetailsform.html",context)

@login_required
def deleteuserdetails(request,pk):
    userdetails=User.objects.get(id=pk)
    
    if request.method=='POST':
        userdetails.delete()
        return redirect('usernames')

    return render(request,"form/delete.html",{'obj':userdetails})

@login_required
def logoutuser(request):
    logout(request)
    return redirect('LoginForm')