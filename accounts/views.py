from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from accounts.models import Profile

# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('index'))


def login(request):
    """Return a log in page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('index'))
            else: 
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if registration_form.is_valid() and profile_form.is_valid():
            user = registration_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user 
            profile.save()
            user = auth.authenticate(username=request.POST['username'],
                                        password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Registered!")
                return render(request, 'index.html')
            else:
                messages.error(request, "Unable to register your account at this time.")
    else:
         registration_form = UserRegistrationForm()
         profile_form = ProfileForm()
    return render(request, 'registration.html', {"registration_form": registration_form, "profile_form": profile_form})


