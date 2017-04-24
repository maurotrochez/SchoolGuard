from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            # return render(request, 'account/register_done.html', {'new_user': new_user})
            return render(request, 'base.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def hello(request):
    return HttpResponse('Hello world')
