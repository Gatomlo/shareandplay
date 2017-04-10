#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Proprietaire,Genre,Jeux,Type

admin.site.register(Proprietaire)
admin.site.register(Genre)
admin.site.register(Jeux)
admin.site.register(Type)
