from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user is not None:

            return HttpResponse('User already exists')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return HttpResponse('User created')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login_auth(request, user)
            return HttpResponse('Logged in successfully')
        else:
            return HttpResponse('Invalid credentials')
