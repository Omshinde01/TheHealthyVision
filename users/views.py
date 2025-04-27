from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, ProfileForm

def home(request):
    return render(request, 'home.html') 

def contactus(request):
    return render(request, 'contactus.html') 

from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()  # Save user
            
            # Check if a profile already exists for this user
            profile, created = Profile.objects.get_or_create(user=user)
            
            # Only update profile if it's newly created
            if created:
                profile.phone = profile_form.cleaned_data.get('phone')
                profile.address = profile_form.cleaned_data.get('address')
                profile.profile_picture = profile_form.cleaned_data.get('profile_picture')
                profile.save()
            
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
        profile_form = ProfileForm()

    return render(request, 'users/register.html', {'form': form, 'profile_form': profile_form})


class UserLoginView(LoginView):
    template_name = 'users/login.html'  # ✅ Points to login page

class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'  # ✅ Points to logout page

from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')  # Redirect to home after logout
