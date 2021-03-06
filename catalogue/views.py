#-*- coding: utf-8 -*-
from django.shortcuts import render, reverse
from catalogue.models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q

@login_required
def accueil(request):
    jeux = Jeux.objects.filter(visible=True)
    genres = Genre.objects.all()
    types = Type.objects.all()
    publics = Public.objects.all()
    edition = False
    onglets = OngletsOuverts.objects.filter(utilisateur=request.user.id)

    return render(request, 'catalogue/catalogue.html', {'jeux': jeux,
                                                        'genres':genres,
                                                        'types':types,
                                                        'edition':edition,
                                                        'publics':publics,
                                                        'onglets':onglets})

@login_required
def mesJeux(request):
    jeux = Jeux.objects.filter(proprietaire=request.user.id)
    genres = Genre.objects.all()
    types = Type.objects.all()
    publics = Public.objects.all()
    edition = True
    onglets = OngletsOuverts.objects.filter(utilisateur=request.user.id)

    return render(request, 'catalogue/catalogue.html', {'jeux': jeux,
                                                        'genres':genres,
                                                        'types':types,
                                                        'edition':edition,
                                                        'publics':publics,
                                                        'onglets':onglets})


@login_required
def nouveauJeu(request):
    form = JeuxForm(request.POST, request.FILES or None)
    if form.is_valid():
        jeu = form.save(commit=False)
        jeu.proprietaire = request.user
        form.save()
        return HttpResponseRedirect(reverse('mesJeux'))

    return render(request, 'catalogue/nouveauJeu.html', locals())

@login_required
def nouveauGenre(request):
    form = GenreForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'catalogue/nouveauGenre.html', locals())

@login_required
def fiche(request,id):
    jeu =  get_object_or_404(Jeux, id=id)
    onglets = OngletsOuverts.objects.filter(utilisateur=request.user.id)
    return render(request, 'catalogue/fiche.html', {'jeu': jeu,
                                                    'onglets':onglets})

@login_required
def ouvrirOnglet(request,id):
    jeu =  get_object_or_404(Jeux, id=id)
    if  not OngletsOuverts.objects.filter(Q(utilisateur=request.user) & Q(jeu=jeu)):
        OngletsOuverts(jeu=jeu, utilisateur=request.user).save()
    onglets = OngletsOuverts.objects.filter(utilisateur=request.user)
    return render(request, 'catalogue/fiche.html', {'jeu': jeu,
                                                    'onglets':onglets})

@login_required
def fermerOnglet(request,id):
    onglet =  get_object_or_404(OngletsOuverts, id=id)
    onglet.delete()
    return HttpResponseRedirect(reverse('accueil'))

@login_required
def profil(request,id):

    profil = get_object_or_404(User, id=id)
    onglets = OngletsOuverts.objects.filter(utilisateur=request.user.id)

    return render(request, 'catalogue/profil.html', {'profil': profil,
                                                     'onglets':onglets})

@login_required
def comfirmer(request,id):
    jeu = get_object_or_404(Jeux, id=id)
    return render(request, 'catalogue/validation.html', {'jeu': jeu})

@login_required
def supprimerJeu(request,id):
    jeu = get_object_or_404(Jeux, id=id)
    if jeu.proprietaire.id == request.user.id:
        jeu.delete()
        return HttpResponseRedirect(reverse('mesJeux'))

@login_required
def cacher(request,id):
    jeu = get_object_or_404(Jeux, id=id)
    if jeu.proprietaire.id == request.user.id:
        if jeu.visible == True:
            jeu.visible = False
        else:
            jeu.visible = True
        jeu.save()
        return HttpResponseRedirect(reverse('mesJeux'))

@login_required
def editerJeu(request,id):
    jeu = get_object_or_404(Jeux, id=id)
    if jeu.proprietaire.id == request.user.id:
        form = JeuxForm(instance=jeu)
        if request.POST:
            form = JeuxForm(request.POST, instance=jeu)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('mesJeux'))
        return render(request, 'catalogue/editerJeu.html', locals(),{'jeu':jeu})

@login_required
def editerProfil(request):
    profil = get_object_or_404(Profil, user_id = request.user.id)
    form1 = ProfilForm(instance=profil)
    form2 = UserForm(instance=request.user)
    if request.POST:
        form1 = ProfilForm(request.POST, instance=profil)
        form2 = UserForm(request.POST, instance=request.user)
        if form1.is_valid():
            form1.save()
        if form2.is_valid():
            form2.save()
        return HttpResponseRedirect(reverse('profil',args=[request.user.id]))
    return render(request, 'catalogue/editerProfil.html', locals())

@login_required
def emprunts(request,id):
    jeu = get_object_or_404(Jeux, id=id)
    emprunts = Emprunt.objects.all()
    form = EmpruntForm(request.POST or None)
    if request.POST:
        form = EmpruntForm(request.POST or None)
        if form.is_valid():
            emprunt = form.save(commit=False)
            emprunt.proprietaire = jeu.proprietaire
            emprunt.emprunteur = request.user
            emprunt.jeu = jeu
            if jeu.proprietaire == request.user:
                emprunt.empruntValide = True
            form.save()
            return HttpResponseRedirect(reverse('accueil'))
    return render(request, 'catalogue/emprunter.html', locals(), {'jeu':jeu,'emprunts':emprunts})

@login_required
def emprunter(request,id,debut,fin):
    jeu = get_object_or_404(Jeux, id=id)
    Emprunt(jeu=jeu,dateDePret=debut,dateDeRetourPrevue=fin, emprunteur=request.user,proprietaire=jeu.proprietaire).save()

    return HttpResponseRedirect(reverse('accueil'))


@login_required
def historique(request):
    historique = Emprunt.objects.filter(Q(proprietaire=request.user.id) | Q(emprunteur=request.user.id))
    return render(request, 'catalogue/historique.html', {'historique':historique})
