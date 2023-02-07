from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login


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
            return HttpResponseRedirect(reverse('index'))      # antes era 'index'
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def profile(request):
    return render(request, 'accounts/profile.html')

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
