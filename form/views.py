from django import contrib
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.db.models import Q
from form.forms import CreateUserForm,UserForm
# create your views here 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Userdetails
from django.http import HttpResponse
# for flash message
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
    

def SignUpForm(request):
    try:
        form1 = CreateUserForm()
        if request.method=='POST':
            form1 = CreateUserForm(request.POST)
            if form1.is_valid():
                form1.save()
                username = form1.cleaned_data.get('username')
                messages.success(request, 'Account is created for ' + username)

                return redirect('LoginForm') 

        context = {}   
        context.update({'form1':form1}) 
        return render(request,"form/SignUpForm.html",context)

    except Exception as e:
        messages.warning(request,f'Username or Password is incorrect !!! :{e}')
    
@login_required
def usernames(request):
    userdetails=User.objects.all()
    for i in userdetails:
        print(i.id)
    current_user = request.user
    
    context={"userdetails":userdetails,"current_user":current_user}
    return render(request,"form/username.html",context)

@login_required
def UserDetails(request,pk):
    # room=None
    # for i in rooms:
    #     if i['id']==int(pk):
    #         room=i
    userdetails=User.objects.get(id=pk)
    context={'userdetails':userdetails}
    return render(request,"form/userdetails.html",context)

@login_required    
def updateUserdetails(request,pk):
    userdetails=User.objects.get(id=pk)
    form=UserForm(instance=userdetails)
    if request.method=='POST':
        form=UserForm(request.POST,instance=Userdetails)
        if form.is_valid():
            form.save()
            return redirect('form/usernames')
        else:
            messages.warning(request,f'Username or Password is incorrect !!! ')


    context={'userdetails':userdetails,'form':form}
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