from django.contrib import admin
from django.urls import path, include
from SimulationEtudiant import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1',include('djoser.urls')),
    path('api/v1',include('djoser.urls.authtoken')),
    path('api/v1',include('SimulationEtudiant.urls'))
]
