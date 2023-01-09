from django.contrib import admin
from django.urls import path, include
from SimulationEtudiant import urls
from SimulationEtudiant.views import voter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1',include('djoser.urls')),
    path('api/v1',include('djoser.urls.authtoken')),
    path('api/v1',include('SimulationEtudiant.urls')),
    # Mon cher miye binani chinda iko na nitumiya 404 à chaque instant
    path('Etudiant/<str:nom>/voter', voter, name='voter')
]
