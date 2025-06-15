from django import forms
from .models import UserProfile, WorkExperience, Education

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
    
class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['position', 'organization', 'skills', 'description', 'joining', 'enddate']
        # help_texts = {
        #     'title': 'e.g. Backend Developer, Intern',
        #     'company': 'e.g. TCS, Infosys',
        #     'description': 'Describe your role and achievements.',
        #     'start_date': 'Format: YYYY-MM-DD',
        #     'end_date': 'Leave blank if still working here.',
        # }
        error_messages = {
            'position': {'required': 'Please enter your job title.'},
            'organization': {'required': 'Please enter the organization name.'},
            'joining': {'required': 'Start date is required.'},
        }
    
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['course', 'institude', 'skills', 'staringDate', 'endingDate', 'cgpa', 'percentage']
        # help_texts = {
        #     'degree': 'e.g. B.Tech, M.Sc, etc.',
        #     'institution': 'e.g. Brainware University',
        #     'field_of_study': 'e.g. Computer Science',
        #     'start_year': 'e.g. 2020',
        #     'end_year': 'Leave blank if currently studying',
        # }
        error_messages = {
            'course': {'required': 'Please enter your degree name.'},
            'institude': {'required': 'Please enter your institution name.'},
            'staringDate': {'required': 'Please provide a start year.'},
        }