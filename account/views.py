from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .models import MyUser as User
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'User created successfully')

            # return render(request, 'account/register_done.html', {'new_user': new_user})
            # return render(request, 'account/list.html', {'new_user': new_user})
            return redirect("list_users")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def list_users(request):
    list_users = User.objects.all()
    return render(request, 'account/list.html', context={'data': list_users})


def home(request):
    return render(request, 'home.html', context={'a': 1})
