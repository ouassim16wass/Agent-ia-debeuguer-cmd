🧠 Agent IA Debugger (Python + Groq)

Cet outil permet de débuguer automatiquement n’importe quel fichier Python en utilisant un modèle IA (Groq).
Il exécute ton script, analyse le traceback, propose des corrections et modifie ton fichier si tu valides.

 Exécution (CLI)

Pour corriger un script :

python iafix.py C:\chemin\script.py


L’outil :

Exécute ton script dans son environnement virtuel

Récupère l’erreur (traceback)

Analyse tout le code avec l’IA

Génère toutes les corrections nécessaires

Te demande :

Appliquer TOUTES les corrections ? (o/n)


Modifie ton fichier si tu réponds oui

 Interface graphique (Streamlit)

Pour une interface simple :

streamlit run app/ui/interface.py


Elle permet de :

choisir un fichier Python

détecter automatiquement le venv

lancer l’analyse IA

afficher l’erreur en couleur

appliquer les corrections d’un clic



⚠️ Améliorations possibles

Détection complète de toutes les erreurs en une seule analyse (logique + runtime)

Patch intelligent multi-fichiers

Mode “Undo” (annuler correction)

Affichage du diff avant/après

Correction automatique sans confirmation
