import django.contrib.auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def home(request):
    count = User.objects.count()
    if request.user.is_authenticated:
        return render(request, 'home.html', {'userCount': count})
    else:
        return redirect('login')




def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            django.contrib.auth.login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm(request.POST)
    return render(request, 'registration/signup.html', {'form': form})
