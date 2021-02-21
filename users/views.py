from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_update = UserUpdateForm(request.POST, instance=request.user)
        u_update_profile = ProfileUpdateForm(request.POST,
                                             request.FILES,
                                             instance=request.user.profile)
        if u_update.is_valid() and u_update_profile.is_valid():
            u_update.save()
            u_update_profile.save()
            messages.success(request, f'Your account info has been updated')
            return redirect('profile')
    else:
        u_update = UserUpdateForm(instance=request.user)
        u_update_profile = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_update': u_update,
        'u_update_profile': u_update_profile
    }

    return render(request, 'profile.html', context)
