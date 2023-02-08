from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UpdateUserForm, UpdateProfileForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            user_group = Group.objects.get(name='Paciente')       # antes era 'Paciente'
            user.groups.add(user_group)
            user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, user)
            return HttpResponseRedirect(reverse('profile'))      # antes era 'index'
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def profile(request):
    if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, instance=request.user)
            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Seus dados foram alterados com sucesso!')
                return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'accounts/profile.html', {'user_form': user_form, 'profile_form': profile_form})

'''
    def signup_psi(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user= form.save()
                user_group = Group.objects.get(name='Psicologo') 
                user.groups.add(user_group)

                return HttpResponseRedirect(reverse('index'))
        else:
            form = UserCreationForm()

        context = {'form': form}
        return render(request, 'accounts/signup_psi.html', context)
'''
