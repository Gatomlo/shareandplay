# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 12:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0008_auto_20170403_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50, verbose_name='Titre')),
                ('contenu', models.TextField(blank=True, null=True, verbose_name='Contenu')),
                ('dateDeCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDeCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateDeRetourPrevue', models.DateTimeField()),
                ('dateDePret', models.DateTimeField()),
                ('dateDeRetour', models.DateTimeField()),
                ('empruntValide', models.BooleanField(default=False)),
                ('jeuRendu', models.BooleanField(default=False)),
                ('emprunteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprunteur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='jeux',
            name='dureeDuPret',
            field=models.IntegerField(null=True, verbose_name='Durée du prêt'),
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='afficheAdresse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='afficheMail',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='afficheTelephone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='pretParDefaut',
            field=models.IntegerField(default=15, verbose_name='Durée des prêts par défaut'),
        ),
        migrations.AlterField(
            model_name='proprietaire',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='emprunt',
            name='jeu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Jeux'),
        ),
        migrations.AddField(
            model_name='emprunt',
            name='proprietaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preteur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='avis',
            name='jeu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Jeux'),
        ),
    ]
