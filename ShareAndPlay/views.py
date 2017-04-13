#-*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from .forms import *
from django.contrib.auth.models import User

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect('catalogue/accueil')
            else: # sinon une erreur sera affichée
                error = True

    else:
        form = ConnexionForm()

    return render(request, 'ShareAndPlay/connect.html', locals())

def deconnexion(request):

    logout(request)

    return redirect('catalogue/accueil')
