from django.urls import path

from . import(
    gestion_auteur, gestion_categorie, gestion_bibliotheque, gestion_adherent, gestion_livre
)
urlpatterns = [

    path('ajout-auteur/', gestion_auteur.ajoutAuteur, name='ajout_auteur'),
    path('auteurs/', gestion_auteur.auteurs, name='liste_auteurs'),
    path('auteur/<int:id>/', gestion_auteur.auteur, name='auteur'),


    path('ajout-categorie/', gestion_categorie.ajoutCategorie, name='ajout_categorie'),
    path('categories/', gestion_categorie.categories, name='liste_categories'),
    path('categorie/<int:id>/', gestion_categorie.categorie, name='categorie'),

    path('ajout-adherent/', gestion_adherent.ajoutAdherent, name='ajout_adherent'),
    path('adherents/', gestion_adherent.adherents, name='liste_adherents'),
    path('adherent/<int:id>/', gestion_adherent.adherent, name='adherent'),

    path('ajout-livre/', gestion_livre.ajoutLivre, name='ajout_livre'),
    path('livres/', gestion_livre.livres, name='liste_livres'),
    path('livre/<int:id>/', gestion_livre.livre, name='livre'),

    path('ajout-bibliotheque/', gestion_bibliotheque.ajoutBibliotheque, name='ajout_bibliotheque'),
    path('bibliotheques/', gestion_bibliotheque.bibliotheques, name='liste_bibliotheques'),
    path('bibliotheque/<int:id>/', gestion_bibliotheque.bibliotheque, name='bibliotheque'),

    
]
