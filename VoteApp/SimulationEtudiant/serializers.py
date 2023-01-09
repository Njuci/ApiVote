from rest_framework import serializers
from .models import Faculte, promotion, Etudiant, Candidats


class FaculteSerial(serializers.ModelSerializer):
    model=Faculte
    fields=(
        "id",
        "codeFac",
        "denomination_extact"        
        )

    
class PromotionSerializer(serializers.ModelSerializer):
    model=promotion
    fields=(
        "id",
        "faclte",
        "codePromotion",
        "denomination_exact_Promo",
        "getFac"
        )


class EtudiantSerial(serializers.ModelSerializer):
    model=Etudiant
    fields=(
        "id",
        "nom",
        "post_nom",
        "prenom",
        "sexe",
        "numMatricule",
        "promotion",
        "statut"
    )

class CandidatSerial(serializers.ModelSerializer):
    model=Candidats
    fields=(
        "id",
        "nom",
        "post_nom",
        "prenom",
        "sexe",
        "numMatricule",
        "promotion",
        "voix"
    )