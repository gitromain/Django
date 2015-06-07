from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg
from datetime import datetime

# Create your models here.
class Recette(models.Model):
    DIFFICULTE = (
        ('0', 'Très facile'), #la première valeur du tuple est stockée en base, la deuxième est affiché pour les widgets
        ('1', 'Facile'),
        ('2', 'Normal'),
        ('4', 'Difficile'),
        ('5', 'Over 9000'),
    )
    TYPE = (
        ('0', 'Apéro'), #la première valeur du tuple est stockée en base, la deuxième est affiché pour les widgets
        ('1', 'Entrée'),
        ('2', 'Plat'),
        ('4', 'Dessert'),
    )
    user = models.ForeignKey(User,default=1,editable=False)
    type_recette = models.CharField(max_length=15, choices=TYPE)
    titre = models.CharField(max_length=50)
    difficulte = models.CharField(max_length=15, choices=DIFFICULTE)
    cout = models.IntegerField()
    photo = models.CharField(max_length=250)
    temps_preparation = models.IntegerField()
    temps_cuisson = models.IntegerField()
    temps_repos = models.IntegerField()

    def calculateAvg(self):
        return Note.objects.filter(id_recette = self).aggregate(Avg('valeur'))

    moyenne = property(calculateAvg)


class Ingredient(models.Model):
    id_recette = models.ForeignKey(Recette)
    type = models.CharField(max_length=50) # légume, viande, ...
    libelle = models.CharField(max_length=50) # le nom de l'ingrédient : carotte, lait, oeuf
    quantite = models.IntegerField()
    unite = models.CharField(max_length=5)

class Etape(models.Model):
    id_recette = models.ForeignKey(Recette)
    libelle = models.TextField()

class Note(models.Model):
    VALEUR_NOTE = (
        (0, 0), #la première valeur du tuple est stockée en base, la deuxième est affiché pour les widgets
        (1, 1),
        (2, 2),
        (4, 4),
        (5, 5),
    )
    user = models.ForeignKey(User, blank=True, null=True)
    id_recette = models.ForeignKey(Recette, blank=True, null=True)
    valeur = models.IntegerField(choices=VALEUR_NOTE)

class Commentaire(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=1)
    id_recette = models.ForeignKey(Recette, blank=True, null=True)
    libelle = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True,default=datetime.now, blank=True, null=True)
