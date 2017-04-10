#-*- coding: utf-8 -*-

from django import forms
from .models import *

class JeuxForm(forms.ModelForm):
    class Meta:
        model = Jeux
        fields = '__all__'

class ProprietaireForm(forms.ModelForm):
    class Meta:
        model = Proprietaire
        fields = ('nomDuProprietaire',)

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
