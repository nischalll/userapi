# core/user/models.py
from django.db import models

from django.contrib.auth.models import  AbstractUser, BaseUserManager, PermissionsMixin


class User(AbstractUser):
    userid = models.IntegerField(null=True,unique=True)
    mobileno = models.CharField(max_length=15)
   
    def __str__(self):
        return f"{self.username}"
    
