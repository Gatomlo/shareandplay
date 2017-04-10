#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.accueil, name="accueil"),  # Permet de créer un nouveau raccourcis d'URL
    url(r'^nouveauJeu$', views.nouveauJeu, name="nouveauJeu"),
    url(r'^nouveauGenre$', views.nouveauGenre, name="nouveauGenre"),
    url(r'^fiche/(?P<id>\d+)$', views.fiche, name="fiche"),
]
