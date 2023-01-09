from django.contrib import admin
from .models import Faculte,promotion,Etudiant,Candidats

class tableFac(admin.ModelAdmin):
    list_display=('codeFac','denomination_extact')
class tablePromotion(admin.ModelAdmin):
    list_display=('faclte','codePromotion','denomination_exact_Promo')
class tablEtudiant(admin.ModelAdmin):
    list_display=('nom','post_nom','prenom','numMatricule', 'statut')

class tablCandidat(admin.ModelAdmin):
    list_display=('nom','post_nom','prenom','numMatricule', 'statut', 'voix')


admin.site.register(Faculte,tableFac)
admin.site.register(promotion,tablePromotion)
admin.site.register(Etudiant,tablEtudiant)
admin.site.register(Candidats, tablCandidat)