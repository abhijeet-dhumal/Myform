from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LoginForm,name="LoginForm"),
    path('signup/', views.register,name="SignUpForm"),
    path('user_dashboard/', views.dashboard,name="dashboard"),
    path('logout/', views.logoutuser, name ='logoutuser'),
    path('usernames/', views.usernames,name="usernames"),
    path('userdetails/<str:pk>/', views.UserDetails,name="userdetails"),
    path('update_details/<str:pk>/',views.updateUserdetails,name="updateuserdetails"),
    path('delete_details/<str:pk>/',views.deleteuserdetails,name="deleteuserdetails")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)