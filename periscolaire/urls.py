from django.urls import path # Importation de la fonction path pour définir les URL patterns
from . import views # Importation des vues du module courant (periscolaire)

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('enfants/', views.liste_enfants, name='liste_enfants'),
    path('activites/', views.liste_activites, name='liste_activites'),
    path('inscriptions/', views.liste_inscriptions, name='liste_inscriptions'),
]