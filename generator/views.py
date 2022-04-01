from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    thepassword = ''

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend('QWERTYUIOPASDFGHJKLZXCVBNM')

    if request.GET.get('numbers'):
        characters.extend('0123456789')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+-=')

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')

# Create your views here.
