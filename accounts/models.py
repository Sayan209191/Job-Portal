from datetime import datetime, timezone
from django.contrib.auth.models import User
from django.db import models
from jobs.models import Job
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default=name)
    address = models.CharField(max_length=255)
    skills = models.TextField()  #  handle this as a comma-separated list
    resume = models.FileField(upload_to='account/resumes/', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='account/profilepicture/', blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    about = models.CharField(max_length=250, blank=True, null=True)
    coins = models.IntegerField(default=1)
    profile_views = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class WorkExperience(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=200, blank=True, null=True)
    postion = models.CharField(max_length=250, blank=True, null=True)
    skills =  models.TextField()
    description = models.TextField() 
    joining = models.DateField()
    enddate = models.DateField(blank=True)
    experience = models.TextField()
    
class Education(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    institude = models.CharField(max_length=250)
    course = models.CharField(max_length=300)
    staringDate = models.DateField()
    endingDate = models.DateField()
    cgpa = models.CharField(max_length=10, blank=True, null=True)
    percentage = models.CharField(max_length=10, blank=True, null=True)


class SavedJob(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    
    
class Project(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=250)
    descrption = models.TextField()
    project_url = models.URLField()
    staring_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    
class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate = models.FileField(upload_to='account/Certicates/', blank=True, null=True)

class AcievementCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    acievement = models.TextField()
    
class AppliedJob(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    savedTime = datetime.now(timezone.utc) 
      
class SocialMediaAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin = models.URLField()
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    github = models.URLField()      