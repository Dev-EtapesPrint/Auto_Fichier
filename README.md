# Automatisation-fichier

# Programme de déplacement de fichiers par semaine

Ce programme Python permet de déplacer des fichiers d'un répertoire source vers un répertoire de destination en les organisant dans des dossiers correspondant aux semaines de l'année.

## Explication étape par étape

1. Import des modules nécessaires : `os` pour les opérations sur le système de fichiers, `shutil` pour les opérations de déplacement de fichiers, et `datetime` pour la manipulation des dates et heures.

2. Définition de la fonction `deplacer_fichiers_par_semaine` avec les paramètres `source` (répertoire source) et `destination` (répertoire de destination).

3. Obtention de la liste des fichiers dans le répertoire source avec `os.listdir(source)`.

4. Itération sur chaque fichier dans la liste.

5. Construction du chemin d'accès complet du fichier avec `os.path.join(source, fichier)`.

6. Obtention de la date de création du fichier avec `os.path.getctime(chemin_fichier)`.

7. Conversion de la date de création en un objet `datetime.datetime` avec `datetime.datetime.fromtimestamp()`.

8. Extraction du numéro de semaine de l'année avec `.isocalendar()[1]`.

9. Création du nom du dossier de destination en utilisant le numéro de semaine, par exemple, "Semaine10" pour la semaine 10.

10. Construction du chemin d'accès complet du dossier de destination avec `os.path.join(destination, nom_dossier)`.

11. Vérification de l'existence du dossier de destination avec `os.path.exists(dossier_destination_semaine)`. Création du dossier s'il n'existe pas avec `os.makedirs(dossier_destination_semaine)`.

12. Déplacement du fichier dans le dossier de destination avec `shutil.move(chemin_fichier, os.path.join(dossier_destination_semaine, fichier))`.

13. Affichage d'un message indiquant le succès du déplacement du fichier.

14. Spécification des chemins d'accès du répertoire source (`repertoire_source`) et du dossier de destination (`dossier_destination`).

15. Appel de la fonction `deplacer_fichiers_par_semaine` avec les chemins d'accès appropriés.

Assurez-vous de remplacer les noms fictifs ("ArriveeFichier" et "SortieFichier") par les chemins d'accès réels correspondant à votre répertoire source et à votre dossier de destination.
