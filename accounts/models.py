from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, phone=None, password=None, **other_fileds):
        if not username:
            raise ValueError("Username is required")
        email  = self.normalize_email(email)
        user = self.model(email=email, username=username, phone=phone , **other_fileds)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(username=username, password=password, **other_fields)
def profile_image_upload_to(instance, filename):
    return f'profiles/{instance.username}/{filename}'

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField( max_length=16, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    birthDate = models.CharField(max_length=10)
    image  = models.ImageField(upload_to=profile_image_upload_to, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username