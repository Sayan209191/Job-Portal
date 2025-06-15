from django.contrib import admin
from accounts.models import UserProfile, WorkExperience, Education, SavedJob, Project, Certificate, SocialMediaAccount

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(SavedJob)
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(SocialMediaAccount)
# admin.site.register()
# admin.site.register(CustomSocialAccount)