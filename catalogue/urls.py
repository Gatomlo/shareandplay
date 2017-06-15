#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^accueil$', views.accueil, name="accueil"),
    url(r'^mesJeux$', views.mesJeux, name="mesJeux"),
    url(r'^nouveauJeu$', views.nouveauJeu, name="nouveauJeu"),
    url(r'^nouveauGenre$', views.nouveauGenre, name="nouveauGenre"),
    url(r'^fiche/(?P<id>\d+)$', views.fiche, name="fiche"),
    url(r'^ouvrirOnglet/(?P<id>\d+)$', views.ouvrirOnglet, name="ouvrirOnglet"),
    url(r'^fermerOnglet/(?P<id>\d+)$', views.fermerOnglet, name="fermerOnglet"),
    url(r'^profil/(?P<id>\d+)$', views.profil, name="profil"),
    url(r'^supprimer/(?P<id>\d+)$', views.supprimerJeu, name="supprimer"),
    url(r'^comfirmer/(?P<id>\d+)$', views.comfirmer, name="comfirmer"),
    url(r'^editer/(?P<id>\d+)$', views.editerJeu, name="editerJeu"),
    url(r'^editerProfil$', views.editerProfil, name="editerProfil"),
    url(r'^emprunts/(?P<id>\d+)$', views.emprunts, name="emprunts"),
    url(r'^cacher/(?P<id>\d+)$', views.cacher, name="cacher"),
    url(r'^historique$', views.historique, name="historique"),
]
