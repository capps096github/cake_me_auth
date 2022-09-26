from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def loginx(request):
    return render(request, 'registration/login.html')


def signup(request):
    return render(request, 'registration/signup.html')


def register(request):
    if request.method == 'POST':
        # get the username, email, password from the request
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # create a new user with the username, email, and password
        user = User.objects.create_user(username, email, password)
        # log in the user
        login(request, user)
        # redirect to the shop page
        return redirect('shop')
    else:
        return render(request, 'registration/register.html')


def shop(request):
    return render(request, 'shop/shop.html')
