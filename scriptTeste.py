def calculer_moyenne(notes):
    """Calculate the average of a list of numbers, returning None for an empty list."""
    if not notes:
        return None
    return sum(notes) / len(notes)

def trouver_max(liste):
    """Return the maximum element of a non‑empty list."""
    if not liste:
        raise ValueError("La liste est vide")
    max_val = liste[0]
    for i in range(1, len(liste)):
        if liste[i] > max_val:
            max_val = liste[i]
    return max_val

def est_pair(nombre):
    """Return True if *nombre* is even, otherwise False."""
    if nombre % 2 == 0:
        return True
    return False

def inverser_texte(texte):
    """Return the reversed string of *texte*."""
    # Utilisation du slicing pour inverser la chaîne
    return texte[::-1]

def compter_voyelles(mot):
    """Count both lower‑case and upper‑case vowels in *mot*."""
    voyelles = "aeiouAEIOU"
    compteur = 0
    for lettre in mot:
        if lettre in voyelles:
            compteur += 1
    return compteur

def multiplier_liste(nombres, facteur):
    """Return a new list where each element of *nombres* is multiplied by *facteur*.
    The original list is left unchanged."""
    return [x * facteur for x in nombres]
def somme_pairs(debut, fin):
    """Return the sum of all even numbers between *debut* and *fin* inclusive."""
    total = 0
    for i in range(debut, fin + 1):
        if i % 2 == 0:
            total += i
    return total

def factorielle(n):
    """Recursive factorial function with correct base case and multiplication."""
    if n <= 0:
        return 1
    return n * factorielle(n - 1)

def diviser(a, b):
    """Return *a* divided by *b*, raising a clear error if *b* is zero."""
    if b == 0:
        raise ZeroDivisionError("Division par zéro")
    return a / b

def chercher_element(liste, element):
    """Return the index of *element* in *liste* or -1 if not found."""
    for i in range(len(liste)):
        if liste[i] == element:
            return i
    return -1

# Tests
print(calculer_moyenne([]))  # Bug test
print(trouver_max([5, 2, 8, 1]))
print(est_pair(4))
print(inverser_texte("hello"))
print(compter_voyelles("BONJOUR"))
print(multiplier_liste([1, 2, 3], 2))
print(somme_pairs(1, 10))
print(factorielle(5))
print(diviser(10, 0))  # Bug test
print(chercher_element([1, 2, 3], 1))
class GestionnaireEtudiants:
    def __init__(self):
        self.etudiants = {}
        self.cours = {}
    
    def ajouter_etudiant(self, id_etudiant, nom, prenom, age):
        """Add a student if the identifier does not already exist."""
        if id_etudiant in self.etudiants:
            print(f"L'étudiant {id_etudiant} existe déjà, aucune action effectuée.")
            return
        self.etudiants[id_etudiant] = {
            'nom': nom,
            'prenom': prenom,
            'age': age,
            'notes': {}
        }
        print(f"Étudiant {prenom} {nom} ajouté!")
        self.cours[code_cours] = {
            'nom': nom_cours,
            'credits': credits,
            'etudiants_inscrits': []
        }
        print(f"Cours {nom_cours} créé!")
    
    def inscrire_etudiant(self, id_etudiant, code_cours):
        """Enroll a student in a course after verifying both exist."""
        if id_etudiant not in self.etudiants:
            print(f"Étudiant {id_etudiant} introuvable.")
            return
        if code_cours not in self.cours:
            print(f"Cours {code_cours} introuvable.")
            return
        etudiant = self.etudiants[id_etudiant]
        cours = self.cours[code_cours]
        if id_etudiant not in cours['etudiants_inscrits']:
            cours['etudiants_inscrits'].append(id_etudiant)
            print(f"Étudiant inscrit au cours {cours['nom']}")
        else:
            print(f"Étudiant déjà inscrit au cours {cours['nom']}")
        etudiant = self.etudiants[id_etudiant]
    def ajouter_note(self, id_etudiant, code_cours, note):
        """Add a note for a student in a given course after validation."""
        if id_etudiant not in self.etudiants:
            print(f"Étudiant {id_etudiant} introuvable.")
            return
        if code_cours not in self.cours:
            print(f"Cours {code_cours} introuvable.")
            return
        if not (0 <= note <= 20):
            print(f"Note {note} invalide, elle doit être entre 0 et 20.")
            return
        self.etudiants[id_etudiant]['notes'][code_cours] = note
        print(f"Note de {note} ajoutée pour l'étudiant {id_etudiant} dans le cours {code_cours}")
    def calculer_moyenne(self, id_etudiant):
        """Calculate the average of all notes of a student, returning None if no notes."""
        if id_etudiant not in self.etudiants:
            raise KeyError(f"Étudiant {id_etudiant} introuvable")
        notes = self.etudiants[id_etudiant]['notes']
        if not notes:
            return None
        total = sum(notes.values())
        moyenne = total / len(notes)
        return moyenne
        moyenne = self.calculer_moyenne(id_etudiant)
    def obtenir_mentions(self, id_etudiant):
        """Return the mention corresponding to the student's average."""
        moyenne = self.calculer_moyenne(id_etudiant)
        if moyenne is None:
            return "Aucune note"
        if moyenne >= 16:
            return "Très bien"
        elif moyenne >= 14:
            return "Bien"
        elif moyenne >= 12:
            return "Assez bien"
        else:
            return "Passable"
        cours = self.cours[code_cours]
    def lister_etudiants_cours(self, code_cours):
        """Return a list of full names of students enrolled in *code_cours*.
        Missing students are ignored."""
        if code_cours not in self.cours:
            raise KeyError(f"Cours {code_cours} introuvable")
        cours = self.cours[code_cours]
        etudiants_inscrits = []
        for id_etudiant in cours['etudiants_inscrits']:
            etudiant = self.etudiants.get(id_etudiant)
            if etudiant:
                etudiants_inscrits.append(f"{etudiant['prenom']} {etudiant['nom']}")
        return etudiants_inscrits
        cours = self.cours[code_cours]
    def calculer_moyenne_cours(self, code_cours):
        """Calculate the average note for a given course, ignoring missing notes.
        Returns None if no notes are available."""
        if code_cours not in self.cours:
            raise KeyError(f"Cours {code_cours} introuvable")
        notes_cours = []
        for id_etudiant in self.cours[code_cours]['etudiants_inscrits']:
            etudiant = self.etudiants.get(id_etudiant)
            if etudiant:
                note = etudiant['notes'].get(code_cours)
                if note is not None:
                    notes_cours.append(note)
        if not notes_cours:
            return None
        moyenne = sum(notes_cours) / len(notes_cours)
        return moyenne
        moyennes = {}
    def meilleurs_etudiants(self, n):
        """Return the top *n* students sorted by descending average.
        Students without notes are ignored."""
        moyennes = {}
        for id_etudiant, info in self.etudiants.items():
            moyenne = self.calculer_moyenne(id_etudiant)
            if moyenne is not None:
                moyennes[id_etudiant] = moyenne
        # Tri décroissant
        tries = sorted(moyennes.items(), key=lambda x: x[1], reverse=True)
        top_n = tries[:n]
        return top_n
def calculer_statistiques(nombres):
    """Return basic statistics for a list of numbers.
    Returns None for all fields if the list is empty."""
    if not nombres:
        return {'moyenne': None, 'variance': None, 'min': None, 'max': None}
    moyenne = sum(nombres) / len(nombres)
    # Variance population (division by len)
    variance = sum((x - moyenne) ** 2 for x in nombres) / len(nombres)
    minimum = min(nombres)
    maximum = max(nombres)
    return {
        'moyenne': moyenne,
        'variance': variance,
        'min': minimum,
        'max': maximum
    }
def filtrer_par_age(etudiants, age_min, age_max):
    resultats = []
def filtrer_par_age(etudiants, age_min, age_max):
    """Return students whose age is between *age_min* and *age_max* inclusive."""
    resultats = []
    for id_etudiant, info in etudiants.items():
        if age_min <= info['age'] <= age_max:
            resultats.append(info)
    return resultats

def formater_nom_complet(prenom, nom):
    # Bug 16: ne gère pas les noms avec espaces ou caractères spéciaux
def formater_nom_complet(prenom, nom):
    """Return a properly formatted full name, handling spaces and special characters."""
    prenom_formate = prenom.strip().capitalize()
    nom_formate = ' '.join(part.upper() for part in nom.strip().split())
    return f"{prenom_formate} {nom_formate}"
# Tests
gestionnaire = GestionnaireEtudiants()

# Ajout d'étudiants
gestionnaire.ajouter_etudiant("E001", "Dupont", "Marie", 20)
gestionnaire.ajouter_etudiant("E002", "Martin", "Pierre", 22)
gestionnaire.ajouter_etudiant("E003", "Bernard", "Sophie", 19)

# Ajout de cours
gestionnaire.ajouter_cours("MATH101", "Mathématiques", 6)
gestionnaire.ajouter_cours("INFO101", "Informatique", 6)
gestionnaire.ajouter_cours("PHY101", "Physique", 4)

# Inscriptions
print("\n--- Inscriptions ---")
gestionnaire.inscrire_etudiant("E001", "MATH101")
gestionnaire.inscrire_etudiant("E001", "INFO101")
gestionnaire.inscrire_etudiant("E002", "MATH101")
gestionnaire.inscrire_etudiant("E002", "PHY101")

# Bug test: inscription avec ID invalide
gestionnaire.inscrire_etudiant("E999", "MATH101")

# Ajout de notes
print("\n--- Ajout de notes ---")
gestionnaire.ajouter_note("E001", "MATH101", 15)
gestionnaire.ajouter_note("E001", "INFO101", 17)
gestionnaire.ajouter_note("E002", "MATH101", 12)

# Bug test: note invalide
gestionnaire.ajouter_note("E002", "PHY101", 25)

# Calcul de moyennes
print("\n--- Moyennes ---")
print(f"Moyenne E001: {gestionnaire.calculer_moyenne('E001'):.2f}")
print(f"Mention E001: {gestionnaire.obtenir_mentions('E001')}")

# Bug test: étudiant sans notes
print(f"Moyenne E003: {gestionnaire.calculer_moyenne('E003'):.2f}")

# Moyenne du cours
print("\n--- Moyenne du cours MATH101 ---")
print(f"Moyenne: {gestionnaire.calculer_moyenne_cours('MATH101'):.2f}")

# Meilleurs étudiants
print("\n--- Top 3 étudiants ---")
top = gestionnaire.meilleurs_etudiants(3)
for id_etudiant, moyenne in top:
    print(f"{id_etudiant}: {moyenne:.2f}")

# Tests de fonctions utilitaires
print("\n--- Tests statistiques ---")
notes = [12, 15, 8, 17, 14]
stats = calculer_statistiques(notes)
print(f"Statistiques: {stats}")

# Bug test: liste vide
stats_vide = calculer_statistiques([])

print("\n--- Test filtrage par âge ---")
resultats = filtrer_par_age(gestionnaire.etudiants, 20, 22)
print(f"Étudiants entre 20 et 22 ans: {len(resultats)}")