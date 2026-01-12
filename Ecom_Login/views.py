from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from Ecom_Login.models import Profile
from Ecom_Login.forms import ProfileForm, SignUpForm

from django.contrib import messages


def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return HttpResponseRedirect(reverse('Ecom_Login:login'))
    return render(request, 'Ecom_Login/sign_up.html', context={'form':form})

def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Ecom_Shop:home'))
        
    return render(request, 'Ecom_Login/login.html', context={'form':form})


@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "You are Logged Out!")
    return HttpResponseRedirect(reverse('Ecom_Shop:home'))


@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully!")
            
            form = ProfileForm(instance=profile)
    return render(request, 'Ecom_Login/change_profile.html', context={'form':form})
    




