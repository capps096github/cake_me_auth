from django.shortcuts import render


def login(request):
    return render(request, 'registration/login.html')


def signup(request):
    return render(request, 'registration/signup.html')


def shop(request):
    return render(request, 'shop/shop.html')
