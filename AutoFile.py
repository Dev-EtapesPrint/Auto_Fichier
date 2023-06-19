import os
import shutil
import datetime

def deplacer_fichiers_par_semaine(source, destination):
    # Obtenir la liste des fichiers dans le répertoire source
    fichiers = os.listdir(source)
    
    for fichier in fichiers:
        chemin_fichier = os.path.join(source, fichier)
        
        # Obtenir la date de création du fichier
        date_creation = datetime.datetime.fromtimestamp(os.path.getctime(chemin_fichier))
        
        # Obtenir le numéro de semaine de l'année
        semaine_annee = date_creation.isocalendar()[1]
        
        # Nom du dossier de destination
        nom_dossier = f"Semaine{semaine_annee}"
        
        # Chemin d'accès complet du dossier de destination
        dossier_destination_semaine = os.path.join(destination, nom_dossier)
        
        # Vérifier si le dossier de destination existe, sinon le créer
        if not os.path.exists(dossier_destination_semaine):
            os.makedirs(dossier_destination_semaine)
            print(f"Dossier {nom_dossier} créé.")
        
        # Déplacer le fichier dans le dossier de destination
        shutil.move(chemin_fichier, os.path.join(dossier_destination_semaine, fichier))
        print(f"Le fichier '{fichier}' a été déplacé vers {dossier_destination_semaine}")

# Chemin d'accès du répertoire source
repertoire_source = "ArriveeFichier"

# Chemin d'accès du dossier de destination
dossier_destination = "SortieFichier"

# Appeler la fonction pour déplacer les fichiers
deplacer_fichiers_par_semaine(repertoire_source, dossier_destination)
