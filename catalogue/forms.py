#-*- coding: utf-8 -*-

from django import forms
from .models import *
from django.contrib.auth.models import User


class JeuxForm(forms.ModelForm):
    class Meta:
        model = Jeux
        exclude = ('proprietaire',)

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        exclude = ('user',)

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
