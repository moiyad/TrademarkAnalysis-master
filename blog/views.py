from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .form import SignupForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as djlogin


def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('login')
    context = {"form": form}
    return render(request, 'signup.html', context)


def login(request):
    form = AuthenticationForm(data=request.POST)
    context = {'login_form': form}
    if form.is_valid():
        djlogin(request, form.get_user())
        user_type = form.get_user().type
        if user_type == '1':
            return redirect('business_company')
        elif user_type == '2':
            return redirect('guest_user')
        return redirect('law_firm')

    return render(request, 'login.html', context)


def user(request, template):
    return render(request, template, {})
