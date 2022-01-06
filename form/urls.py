from django.urls import path
from . import views


urlpatterns = [
    path('', views.LoginForm,name="LoginForm"),
    path('signup/', views.SignUpForm,name="SignUpForm"),
    path('logout/', views.logoutuser, name ='logoutuser'),
    path('usernames/', views.usernames,name="usernames"),
    path('userdetails/<str:pk>/', views.UserDetails,name="userdetails"),
    path('update_details/<str:pk>/',views.updateUserdetails,name="updateuserdetails"),
    path('delete_details/<str:pk>/',views.deleteuserdetails,name="deleteuserdetails")
]