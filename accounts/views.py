from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('/')  # Redirect to the homepage or dashboard
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/login')

    return render(request, 'account/login.html')  


# logout
def handlelogout(request):
    logout(request)
    messages.info(request, "Logout Successful")
    return redirect('/login')
