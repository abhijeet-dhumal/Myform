from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name="home"),
    path('doctor_login/', views.DoctorLoginForm,name="DoctorLoginForm"),
    path('patient_login/', views.PatientLoginForm,name="PatientLoginForm"),
    path('doctor_signup/', views.doctor_registerPage,name="doctor_registerPage"),
    path('patient_signup/', views.patient_registerPage,name="patient_registerPage"),
    # path('user_dashboard/', views.dashboard,name="dashboard"),
    path('logout/', views.logoutuser, name ='logoutuser'),
    path('patient_usernames/', views.patientusernames,name="patientusernames"),
    path('doctor_usernames/', views.doctorusernames,name="doctorusernames"),
    path('doctor_userdetails/<str:pk>/', views.doctor_details,name="doctordetails"),
    path('patient_userdetails/<str:pk>/', views.patient_details,name="patientdetails"),
    path('update_doctor_details/<str:pk>/',views.updatedoctordetails,name="updatedoctordetails"),
    path('update_patient_details/<str:pk>/',views.updatepatientdetails,name="updatepatientdetails"),
    path('delete_details/<str:pk>/',views.deletedoctordetails,name="deletedoctordetails"),
    path('delete_details/<str:pk>/',views.deletepatientdetails,name="deletepatientdetails"),

    path('blogs_view/',views.blogs_view,name="blogs_view"),
    path('blogs_drafts/',views.blogs_drafts,name="blogs_drafts"),
    path('blogs_update/<str:pk>',views.blogs_update,name="blogs_update"),

    path('doctors_list/', views.doctorslist,name="doctorslist"),
    path('appointment_form/', views.appointment_form,name="appointment_form"),
    path('appointments/', views.appointments,name="appointments")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)