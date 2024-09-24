from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    skills = models.TextField()  # Assume you handle this as a comma-separated list
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
