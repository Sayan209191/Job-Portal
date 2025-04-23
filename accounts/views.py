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
from .models import UserProfile


# sign up 
def signup(request):
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

    return render(request, "account/signup.html")


# sign in
def handlelogin(request):
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
    return render(request, 'account/profile-view.html', {'user_profile': user_profile})

# Edit Profile
@login_required
def profile_edit(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'account/edit-profile.html', {'form': form})
