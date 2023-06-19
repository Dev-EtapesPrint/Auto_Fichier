import os
import shutil
import datetime

def deplacer_fichier_par_semaine(source, destination):
    # Obtenir la date de création du fichier
    date_creation = datetime.datetime.fromtimestamp(os.path.getctime(source))
    
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
    shutil.move(source, os.path.join(dossier_destination_semaine, os.path.basename(source)))
    print(f"Le fichier a été déplacé vers {dossier_destination_semaine}")

# Chemin d'accès du fichier source
fichier_source = "/chemin/vers/le/fichier/source.txt"

# Chemin d'accès du dossier de destination
dossier_destination = "/chemin/vers/le/dossier/destination"

# Appeler la fonction pour déplacer le fichier
deplacer_fichier_par_semaine(fichier_source, dossier_destination)
