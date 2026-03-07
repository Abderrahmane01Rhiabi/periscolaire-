from django.shortcuts import render
from .models import Enfant, Activite, Inscription

# Create your views here.

# Vue qui affiche la liste de tous les enfants
def liste_enfants(request):
    enfants = Enfant.objects.all() # Récupère tous les enfants de la base de données
    return render(request, 'periscolaire/enfants.html', {'enfants': enfants}) # Rend la page enfants.html en passant la liste des enfants dans le contexte

# Vue qui affiche la liste de toutes les activités
def liste_activites(request):
    activites = Activite.objects.all()
    return render(request, 'periscolaire/activites.html', {'activites': activites})

# Vue qui affiche la liste de toutes les inscriptions
def liste_inscriptions(request):
    inscriptions = Inscription.objects.all()
    return render(request, 'periscolaire/inscriptions.html', {'inscriptions': inscriptions})

def accueil(request):
    return render(request, 'periscolaire/accueil.html', {
        'nb_enfants': Enfant.objects.count(),
        'nb_activites': Activite.objects.count(),
        'nb_inscriptions': Inscription.objects.count(),
    })