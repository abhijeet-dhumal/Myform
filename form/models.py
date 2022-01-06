from django.db import models
from django.contrib.auth.models import PermissionsMixin, User, UserManager
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# # create email verification 
# class CreateUserManager(BaseUserManager):
#     def _create_user(self,email,password,first_name,last_name,mobile, **extra_fields):
#         if not email:
#             raise ValueError("Email must be provided")
#         if not password:
#             raise ValueError("Password is not provided")

#         user=self.model(
#             email=self.normalize_email(email),
#             first_name=first_name,
#             last_name=last_name,
#             mobile=mobile,
#             **extra_fields
#         )

#         user.set_password(password)
#         user.save(using=self.db)
#         return user 

#     def create_user(self,email,password,first_name,last_name,mobile, **extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_active',True)
#         extra_fields.setdefault('is_superuser',False)
#         return self._create_user(email,password,first_name,last_name,mobile,**extra_fields)

#     def create_superuser(self,email,password,first_name,last_name,mobile, **extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_active',True)
#         extra_fields.setdefault('is_superuser',True)
#         return self._create_user(email,password,first_name,last_name,mobile,**extra_fields)

# class User(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(
#         db_index=True,
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     first_name=models.CharField(max_length=240)
#     last_name=models.CharField(max_length=240)
#     mobile=models.CharField(max_length=50)
#     address=models.CharField(max_length=540)
#     is_staff=models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects=UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['date_of_birth']

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin

# Create your models here.
class Userdetails(models.Model):
    host=models.OneToOneField(User,on_delete=CASCADE,null=True)
    name=models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    address=models.TextField(max_length=500,null=True)
    
    description=models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    

    # class Meta:
    #     ordering=['-updated','-created']
    def __str__(self):
        return self.name

