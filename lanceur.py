import schedule
import subprocess
import time
from datetime import datetime

def run_verification():
    # Appeler le script de vérification en tant que processus externe
    subprocess.run(["python3", "AutoFile.py"])

    # ---------- Paramétrage date/heure actuel ----------
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Action exécutée à {current_time}")

# Planifiez l'exécution de la vérification deux fois par jour

schedule.every().minute.do(run_verification)

# Boucle d'exécution pour vérifier les tâches planifiées
while True:
    schedule.run_pending()
    time.sleep(1)
