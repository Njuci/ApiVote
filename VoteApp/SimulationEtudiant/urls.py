from django.urls import path,include
from SimulationEtudiant import views

urlpatterns = [
    path('Facdispo/',views.FaculteDispo.as_view()),
    path('promotionDispo/',views.PromotionDispo.as_view()),
    path('EtudiantDisp/',views.EtudiantDisp.as_view()),
]

