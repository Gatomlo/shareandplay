#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Profil,Genre,Jeux,Type,Public, Emprunt

admin.site.register(Profil)
admin.site.register(Genre)
admin.site.register(Jeux)
admin.site.register(Type)
admin.site.register(Public)
admin.site.register(Emprunt)
