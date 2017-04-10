#-*- coding: utf-8 -*-
from django.shortcuts import render
from catalogue.models import *
from .forms import *

def accueil(request):
    jeux = Jeux.objects.all()

    return render(request, 'catalogue/accueil.html', {'jeux': jeux})

def nouveauJeu(request):
    form = JeuxForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'catalogue/nouveauJeu.html', locals())

def nouveauGenre(request):
    form = GenreForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'catalogue/nouveauGenre.html', locals())

def fiche(request,id):
    jeu = Jeux.objects.get(id=id)

    return render(request, 'catalogue/fiche.html', {'jeu': jeu})
