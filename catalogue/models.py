#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Jeux(models.Model):
    nomDuJeu = models.CharField(max_length=50,verbose_name="Nom du jeu")
    description = models.TextField(null=True,blank=True)
    dateDeCreation = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de création")
    genre = models.ManyToManyField('Genre')
    typeDeJeu = models.ManyToManyField('Type',verbose_name="Type de jeu")
    public = models.CharField(max_length=50)
    nombreDeJoueurMin = models.IntegerField(verbose_name="Nombre de joueur minimum",null=True,blank=True)
    nombreDeJoueurMax = models.IntegerField(verbose_name="Nombre de joueur maximum",null=True,blank=True)
    dureeMin = models.IntegerField(verbose_name="Durée minimum",null=True,blank=True)
    dureeMax = models.IntegerField(verbose_name="Durée maximum",null=True,blank=True)
    image = models.ImageField(verbose_name="Image",upload_to="photos_jeux/",blank=True)
    extension = models.BooleanField(default=False)
    proprietaire = models.ForeignKey('auth.User')
    disponible = models.BooleanField(default=True)
    pretable = models.BooleanField(default=True)
    dureeDuPret = models.IntegerField(verbose_name="Durée du prêt",null=True,blank=True)

    def __str__(self):
        return self.nomDuJeu

class Genre(models.Model):
    nomDuGenre = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.nomDuGenre

class Type(models.Model):
    nomDuType = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.nomDuType

class Avis(models.Model):
    titre = models.CharField(max_length=50,verbose_name="Titre")
    contenu = models.TextField(null=True,blank=True,verbose_name="Contenu")
    auteur = models.ForeignKey('auth.User')
    jeu = models.ForeignKey('Jeux')
    dateDeCreation = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de création")

    def __str__(self):
        return self.titre

class Emprunt(models.Model):
    proprietaire = models.ForeignKey('auth.User', related_name='preteur')
    emprunteur = models.ForeignKey('auth.User', related_name='emprunteur')
    jeu  = models.ForeignKey('Jeux')
    dateDeCreation = models.DateField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de création")
    dateDeRetourPrevue = models.DateField()
    dateDePret = models.DateField()
    dateDeRetour = models.DateField(null=True,blank=True)
    empruntValide = models.BooleanField(default=False)
    jeuRendu = models.BooleanField(default=False)

    def __str__(self):
        return self.empruntValide

class Profil(models.Model):
    user = models.OneToOneField('auth.User',related_name='profil')
    avatar = models.ImageField(verbose_name="Image",upload_to="avatars/")
    telephone = models.CharField(max_length=15)
    rue = models.CharField(max_length=50)
    numero = models.IntegerField()
    codePostal = models.IntegerField()
    commune = models.CharField(max_length=50)
    afficheMail = models.BooleanField(default=False,verbose_name="Afficher Email")
    afficheTelephone = models.BooleanField(default=False,verbose_name="Afficher téléphone")
    afficheAdresse = models.BooleanField(default=False,verbose_name="Afficher adresse")
    pretParDefaut = models.IntegerField(default=15,verbose_name="Durée des prêts par défaut")

    def __str__(self):
        return self.user.username
