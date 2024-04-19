import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255) 
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255) 
    profile_pic = models.ImageField(upload_to="thumbnail/img/user/")


    class Meta:
        db_table = 'auth_user'

    # Admin fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
class UserVerification(models.Model):
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=20, blank=True, null=True)

    def generate_verification_code(self):
        self.verification_code = get_random_string(length=6, allowed_chars='0123456789')
        self.save()

    def __str__(self) -> str:
        return self.email