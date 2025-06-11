from datetime import datetime, timedelta
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.views.generic import View
from .forms import UserProfileForm
from .models import UserProfile, WorkExperience, Education, SavedJob, Project, Certificate, AcievementCertificate, AppliedJob, SocialMediaAccount, LoginActivity
from django.utils.timezone import now
from .models import AppliedJob
from collections import defaultdict

# sign up 
def signup(request):
    
    try:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['pass1']
            confirm_password = request.POST['pass2']
            
            if password != confirm_password:
                messages.warning(request, "Passwords do not match")
                return render(request, 'account/signup.html')                   
            
            try:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "Email is already taken")
                    return render(request, 'account/signup.html')
            except Exception as identifier:
                pass

            user = User.objects.create_user(username=email, email=email, password=password)
            user.is_active = True
            user.save()

            messages.success(request, "Sign up successful! You can now log in.")
            return redirect('/auth/login')
    except Exception as identifier:
        pass
    finally :  
        return render(request, "account/signup.html")
        

    


# sign in
def handlelogin(request):
    try:
        if request.method == "POST":
            username = request.POST['email']
            password = request.POST['password']
            
            # Debugging: Print the username and password to check the input
            print(f"Attempting login with email: {username} and password: {password}")
            
            # Authenticate user with the given username and password
            user = authenticate(username=username, password=password)

            # Debugging: Print user object to check if authentication is successful
            print(f"Authenticated user: {user}")

            if user is not None:
                login(request, user)
                messages.success(request, "Login Successful")
                return redirect('/')  # Redirect to the homepage
            else:
                messages.error(request, "Invalid Credentials")
                return redirect('/auth/login')
    except Exception as identifier:
        
        pass
    finally : 

        return render(request, 'account/login.html')



# logout
def handlelogout(request):
    logout(request)
    messages.info(request, "Logout Successful")
    return redirect('/')


class RequestResetEmailView(View):
    def get(self,request):
        return render(request,'account/request-reset-email.html')
    
    def post(self,request):
        try:
            email=request.POST['email']
            user=User.objects.filter(email=email)

            if user.exists():
                # current_site=get_current_site(request)
                email_subject='[Reset Your Password]'
                message=render_to_string('account/reset-user-password.html',{
                    'domain':'127.0.0.1:8000',
                    'uid':urlsafe_base64_encode(force_bytes(user[0].pk)),
                    'token':PasswordResetTokenGenerator().make_token(user[0])
                })

                email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
            
                email_message.send(fail_silently=False)
                messages.info(request, "We have sent you a link to reset your password.")
                return redirect('/auth/login')
                # return render(request,'account/request-reset-email.html')
            else:
                messages.error(request, "No user exists with the provided email.")
            return render(request,'account/request-reset-email.html')
        except Exception as e:
            messages.error(request, f"Email failed to send: {e}")

class SetNewPasswordView(View):
    def get(self,request,uidb64,token):
        context = {
            'uidb64':uidb64,
            'token':token
        }
        try:
            user_id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=user_id)

            if  not PasswordResetTokenGenerator().check_token(user,token):
                messages.warning(request,"Password Reset Link is Invalid")
                return render(request,'account/request-reset-email.html')

        except DjangoUnicodeDecodeError as identifier:
            messages.error(request,"Invalid link.")
            return render(request,'account/request-reset-email.html')

        return render(request,'account/set-new-password.html',context)

    def post(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token
        }
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        
        if password != confirm_password:
            messages.warning(request, "Passwords do not match")
            return render(request, 'account/set-new-password.html', context)

        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)

            # Set new password and save
            user.set_password(password)
            user.save()

            messages.success(request, "Password reset successful. Please login with your new password.")
            return redirect('/auth/login')

        except User.DoesNotExist:
            messages.error(request, "Invalid user.")
            return render(request, 'account/set-new-password.html', context)

        except DjangoUnicodeDecodeError:
            messages.error(request, "Something went wrong. Please try again.")
            return render(request, 'account/set-new-password.html', context)

# View Profile
@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    user = get_object_or_404(User, id=user_profile.user_id)
    profile = UserProfile.objects.filter(user=user).first()
    
    # Split skills before sending to template
    if profile and profile.skills:
        profile.skills = [skill.strip() for skill in profile.skills.split(',') if skill.strip()]

    context = {
        'user': user,
        'profile': profile,
        'work_experiences': WorkExperience.objects.filter(user=user).order_by('-id'),
        'educations': Education.objects.filter(user=user).order_by('-id'),
        'saved_jobs': SavedJob.objects.filter(user=user),
        'projects': Project.objects.filter(user=user).order_by('-id'),
        'certificates': Certificate.objects.filter(user=user),
        'achievements': AcievementCertificate.objects.filter(user=user),
        'applied_jobs': AppliedJob.objects.filter(user=user),
        'social_accounts': SocialMediaAccount.objects.filter(user=user).first(),
    }
    context['activity_data'] = json.dumps(get_login_streak_data(request.user))

    return render(request, 'account/profile-view.html', context)

    # return render(request, 'account/profile-view.html')

# Edit Profile
@login_required
def profile_edit(request):
    # user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    # if request.method == 'POST':
    #     form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile_view')
    # else:
    #     form = UserProfileForm(instance=user_profile)

    # return render(request, 'account/edit-profile.html', {'form': form})
    return render(request, 'account/edit-profile.html')


def get_login_streak_data(user):
    today = datetime.today().date()
    
    # GitHub streak calendars start on Sunday, so find last Sunday
    days_since_sunday = today.weekday() + 1  # Monday=0, Sunday=6 → 7
    last_sunday = today - timedelta(days=days_since_sunday % 7)

    start_date = last_sunday - timedelta(weeks=52)  # 52 weeks to cover 1 year

    raw_logins = LoginActivity.objects.filter(
        user=user,
        login_time__date__gte=start_date
    )

    login_counts = defaultdict(int)
    for log in raw_logins:
        login_counts[log.login_time.date()] += 1

    result = []
    for i in range(7 * 53):  # 53 weeks to include partial weeks
        date = start_date + timedelta(days=i)
        result.append({
            "date": date.isoformat(),
            "count": login_counts[date]
        })

    return result