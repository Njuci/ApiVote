from django.shortcuts import render
from .serializers import FaculteSerial, PromotionSerializer, EtudiantSerial
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Faculte,promotion,Etudiant, Candidats
from django.shortcuts import render, get_object_or_404, redirect


class FaculteDispo(APIView):
    def get(self,request,format=None):
        facDispo=Faculte.objects.all()
        serializer=FaculteSerial(facDispo,many=True)
        return Response(serializer.data)


class PromotionDispo(APIView):
    def get(self,request,format=None):
        prmDisp=promotion.objects.all()
        serializer=PromotionSerializer(prmDisp,many=True)
        return Response(serializer.data)


class EtudiantDisp(APIView):
    def get(self,request,format=None):
        etudiantDisp=Etudiant.objects.all()
        serializer=EtudiantSerial(etudiantDisp,many=True)
        return Response(serializer.data)


def voter(request, nom):
    candidat = get_object_or_404(Candidats, nom=nom)
    etudiant = request.Etudiant
    if etudiant.statut != True:
        candidat.voix += 1
        etudiant.statut = True
    return 