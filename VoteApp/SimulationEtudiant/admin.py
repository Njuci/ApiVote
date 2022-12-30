from django.contrib import admin
from .models import Faculte,promotion,Etudiant

class tableFac(admin.ModelAdmin):
    list_display=('codeFac','denomination_extact')
class tablePromotion(admin.ModelAdmin):
    list_display=('faclte','codePromotion','denomination_exact_Promo')
class tablEtudiant(admin.ModelAdmin):
    list_display=('nom','post_nom','prenom','numMatricule')


admin.site.register(Faculte,tableFac)
admin.site.register(promotion,tablePromotion)
admin.site.register(Etudiant,tablEtudiant)
