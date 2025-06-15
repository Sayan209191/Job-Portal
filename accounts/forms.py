from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'address', 'skills', 'resume', 'profile_picture', 'mobile_number', 'about', 'username']

    def clean_resume(self):
        resume = self.cleaned_data.get('resume', False)

        if resume:
            if not resume.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are accepted for resumes.")
            if resume.size > 2 * 1024 * 1024:
                raise forms.ValidationError("Resume file size should be under 2MB.")

        return resume

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number', '')

        if mobile_number and not mobile_number.isdigit():
            raise forms.ValidationError("Mobile number must contain only digits.")
        
        if mobile_number and (len(mobile_number) < 10 or len(mobile_number) > 15):
            raise forms.ValidationError("Enter a valid mobile number (10-15 digits).")
        
        return mobile_number
