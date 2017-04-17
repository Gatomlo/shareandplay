#-*- coding: utf-8 -*-

from django import forms
from .models import *

class JeuxForm(forms.ModelForm):
    class Meta:
        model = Jeux
        exclude = ('proprietaire',)

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
