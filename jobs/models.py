from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

#from .managers import CustomUserManager
from .choices import CHOICES_ADMIN

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique = True)
    userType = models.CharField(max_length=9, choices=CHOICES_ADMIN, default='Student')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #objects = CustomUserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')

class Post(models.Model):
    title = models.CharField(max_length=100)
    requirements = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title