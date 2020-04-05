from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def acceuil(request):
    return render(request, 'base.html')


@login_required
def welcome(request):
    return render(request, 'pro_it/welcome.html')
