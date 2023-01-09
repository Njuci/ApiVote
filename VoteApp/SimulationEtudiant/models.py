from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import *


class Faculte(models.Model):
    codeFac = models.CharField(max_length=10, unique=True)
    denomination_extact = models.TextField()

    # LogoFac = models.ImageField(null=True)
    # les designers vont juger cette affaire de photo

    class Meta:
        ordering = ['codeFac']

    def __str__(self):
        return self.codeFac

    def get__str__(self):
        return self.__str__()


class promotion(models.Model):
    faclte = models.ForeignKey(Faculte, null=False, on_delete=models.CASCADE)
    # on pourrai utiliser TextChoise mais FoeignKey est adapté dans notre cas ici
    codePromotion = models.CharField(max_length=15, unique=True)
    denomination_exact_Promo = models.TextField()

    class Meta:
        ordering = ['codePromotion']

    def __str__(self):
        return self.codePromotion

    def getFac(self):
        # la fonction get__str__() n`était pas définie, je l' ai définie dans le fichier related.py
        return self.faclte.get__str__()


class Etudiant(models.Model):
    Sx = (
        ('m', 'masculin'),
        ('f', 'feminin'),
    )
    nom = models.CharField(max_length=60)
    post_nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60, null=True)
    sexe = models.CharField(max_length=9, choices=Sx)
    numMatricule = models.CharField(unique=True, max_length=26)
    # cherche un moyen que l' on aie seulement l'année
    # ===> voila un moyen pour avoir l'annee actuelle
    #annneFin = models.DateField(datetime.now().year)
    """anneeFin = models.DateField(auto_now=True)
    anneDebut = models.DateField(auto_now=True)"""
    # on a pas mis la faculté parce qu' on l' a déjà à partir de la promotion
    promotion = models.ForeignKey(promotion, on_delete=models.CASCADE)
    # ici un champ booléen de vote
    statut = models.BooleanField(default=False)
    # il y aura une photo ces sont nos designer vont juger
    # Nous en discuterons une fois on se rencontre
    # mais ce modèle est à titre expérimental on prendra tous ces données sur une api de l' univ

    class Meta:
        ordering = ['promotion', 'nom']

    def __str__(self):
        return self.numMatricule


class Candidats(Etudiant):
    voix = models.IntegerField(default=0)