#Projet django site de recettes de cuisine

### Thème
Le thème de l'application : http://luiszuno.com/themes/nova/

###Modèles :

L'objet recette à 1 foreign key :
- l'user

L'objet ingrédient à 1 foreign key :
- la recette

L'objet etape à 1 foreign key :
- la recette

L'objet note à 2 foreign key :
- l'user
- la recette

L'objet commentaire à 2 foreign key :
- la recette

La recette contient 1 une plusieurs ingrédients, étapes, notes, commentaires.

###Installation des données :



###Compte utilisateur :

 Les mot de passe des utilisateurs sont égaux aux identifiants
 Il y a 1 superuser :
 - Login : admin, mot de passe : admin

#BILAN

Fonctions non réalisés : 

- modifier/supprimer recette
- rechercher
- JS permettant l'ajout d'un ingrédient/etape (3 par défaut)
