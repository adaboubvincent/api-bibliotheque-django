from django.db import models

# Create your models here.



class Auteur(models.Model):
	nom = models.CharField(max_length=150, verbose_name="Nom de l'auteur ")
	prenom = models.CharField(max_length=150, verbose_name="Prénom de l'auteur")

class Categorie(models.Model):
    titre = models.CharField(max_length=150, verbose_name="Titre de la categorie ")
    description = models.TextField(max_length=150, verbose_name="Description de la catégorie")


class Livre(models.Model):
    titre = models.CharField(max_length=150, verbose_name="Titre du livre ")
    categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE, related_name="id_categorie")
    auteur = models.ForeignKey(Auteur, on_delete = models.CASCADE, related_name="id_auteur")
    editeur = models.CharField(max_length=150, verbose_name="Editeur du livre ")

class Adherent(models.Model):
    nom = models.CharField(max_length=150, verbose_name="Nom de l'adhérent ")
    prenom = models.CharField(max_length=150, verbose_name="Prénom de l'adhérent")
    telephone = models.CharField(max_length=150, verbose_name="Téléphone de l'adhérent")
    email = models.EmailField(verbose_name="Email de l'adhérent")


class Bibliotheque(models.Model):
    adherent = models.ForeignKey(Adherent, on_delete = models.CASCADE, related_name="id_adherent")
    livre = models.ForeignKey(Livre, on_delete = models.CASCADE, related_name="id_livre")
    dateRetour = models.DateField()
    datePris = models.DateField(auto_now_add = True)
    
