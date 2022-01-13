""" This module contains the investisment class """
from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Investissement(models.Model):
    """ This class contains the essential fields for the investisment model """
    titreoperation = models.CharField(_('titre operation'), max_length=200, null=True)
    entreprise = models.CharField(_('entreprise'), max_length=200, null=True)
    annee_de_livraison  = models.CharField(_('annee de livraison'), max_length=200, null=True)
    ville = models.CharField(_('ville'), max_length=200, null=True)
    mandataire = models.CharField(_('mandaaire'), max_length=200, null=True)
    ppi = models.CharField(_('ppi'), max_length=200, null=True)
    lycee = models.CharField(_('lyce'), max_length=200, null=True)
    notification_du_marche = models.CharField(_('notification du marche'), max_length=200,null=True)
    codeuai = models.CharField(_('codeuai'), max_length=200, null=True)
    longitude = models.FloatField(_('longitude'), null=True)
    etat_d_avancement = models.CharField(_('etat_d_avancement'), max_length=200, null=True)
    montant_des_ap_votes_en_meu = models.FloatField(_('montant des ap votes en meu'), null=True)
    cao_attribution = models.CharField(_('cao_attribution'), max_length=200, null=True)
    latitude = models.FloatField(_('latitude'), null=True)
    maitrise_d_oeuvre = models.CharField(_('maitrise_d_oeuvre'), max_length=200, null=True)
    mode_de_devolution = models.CharField(_('mode_de_devolution'), max_length=200, null=True)
    annee_d_individualisation = models.CharField(_('annee_d_indivi'), max_length=200, null=True)
    enveloppe_prev_en_meu = models.FloatField(_('enveloppe prev en meu'), null=True)
    nombre_de_lots = models.IntegerField(_('nombre_de_lots'), null=True)
    