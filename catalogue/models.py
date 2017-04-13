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
    nombreDeJoueurMin = models.IntegerField(verbose_name="Nombre de joueur minimum",null=True)
    nombreDeJoueurMax = models.IntegerField(verbose_name="Nombre de joueur maximum",null=True)
    dureeMin = models.IntegerField(verbose_name="Durée minimum",null=True)
    dureeMax = models.IntegerField(verbose_name="Durée maximum",null=True)
    image = models.ImageField(verbose_name="Image",upload_to="photos_jeux/")
    extension = models.BooleanField(default=False)
    proprietaire = models.ForeignKey('auth.User')
    disponible = models.BooleanField(default=True)
    pretable = models.BooleanField(default=True)
    dureeDuPret = models.IntegerField(verbose_name="Durée du prêt",null=True)

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
    dateDeCreation = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de création")
    dateDeRetourPrevue = models.DateTimeField()
    dateDePret = models.DateTimeField()
    dateDeRetour = models.DateTimeField()
    empruntValide = models.BooleanField(default=False)
    jeuRendu = models.BooleanField(default=False)

    def __str__(self):
        return self.empruntValide

class Proprietaire(models.Model):
    user = models.ForeignKey('auth.User')
    nomDuProprietaire = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    rue = models.CharField(max_length=50)
    numero = models.IntegerField()
    codePostal = models.IntegerField()
    commune = models.CharField(max_length=50)
    afficheMail = models.BooleanField(default=False)
    afficheTelephone = models.BooleanField(default=False)
    afficheAdresse = models.BooleanField(default=False)
    pretParDefaut = models.IntegerField(default=15,verbose_name="Durée des prêts par défaut")

    def __str__(self):
        return self.nomDuProprietaire
