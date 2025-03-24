from django.db import models
# from djongo import models

# Create your models here.

class Company(models.Model) :
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    JOB_TYPES = [
        ('Govt', 'Government'),
        ('Private', 'Private'),
        ('Internship-Govt', 'Government Internship'),
        ('Internship-Private', 'Private Internship'),
    ]
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    skills_required = models.TextField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_posted = models.DateField()
    experience_required = models.CharField(max_length=100, null=True, blank=True)
    views = models.IntegerField(default=0)
    salary = models.CharField(max_length=100, null=True, blank=True)
    application_count = models.IntegerField(default=0)
    application_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


