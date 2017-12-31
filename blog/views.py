from django.shortcuts import render, redirect
from .form import SignupForm
import time
import core.templates.core
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as djlogin


# def for register account
def signup(request):
    form = SignupForm(request.POST or None)
    # if the account accepted
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('success',)
    context = {"form": form}
    # send the dictionary to HTML
    return render(request, 'signup.html', context)


# def for login account
def login(request):
    form = AuthenticationForm(data=request.POST)
    context = {'login_form': form}
    if form.is_valid():
        djlogin(request, form.get_user())
        user_type = form.get_user().type
        # type of the account for login
        if user_type == '1':
            return redirect('home')
        elif user_type == '2':
            return redirect('guest_user')
        return redirect('home')
    return render(request, 'login.html', context)


def user(request, template):
    return render(request, template, {})


def success(request):
    return render(request, 'success_account.html', )
