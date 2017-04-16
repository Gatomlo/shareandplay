#-*- coding: utf-8 -*-
from django.shortcuts import render, reverse
from catalogue.models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

def accueil(request):
    jeux = Jeux.objects.all()

    return render(request, 'catalogue/accueil.html', {'jeux': jeux})

@login_required
def mesJeux(request):

    jeux = Jeux.objects.filter(proprietaire=request.user.id)

    return render(request, 'catalogue/mesJeux.html', {'jeux': jeux})

@login_required
def nouveauJeu(request):
    form = JeuxForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('mesJeux'))

    return render(request, 'catalogue/nouveauJeu.html', locals())

@login_required
def nouveauGenre(request):
    form = GenreForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'catalogue/nouveauGenre.html', locals())

def fiche(request,id):
    jeu =  get_object_or_404(Jeux, id=id)

    return render(request, 'catalogue/fiche.html', {'jeu': jeu})

@login_required
def profil(request,id):

    profil = get_object_or_404(User, id=id)

    return render(request, 'catalogue/profil.html', {'profil': profil})

@login_required
def comfirmer(request,id):
    jeu = get_object_or_404(Jeux, id=id)
    return render(request, 'catalogue/validation.html', {'jeu': jeu})

@login_required
def supprimer(request,id):
    jeu = get_object_or_404(Jeux, id=id)
    if jeu.proprietaire.id == request.user.id:
        jeu.delete()
        return HttpResponseRedirect(reverse('mesJeux'))
