import json

def validate_json(text: str) -> dict:
    """
    Vérifie que la réponse IA est un JSON valide
    et qu’il contient les champs obligatoires.
    """
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        raise ValueError("JSON invalide renvoyé par l’IA.")

    required = ["explanation", "fixable", "reason", "patches"]
    for key in required:
        if key not in data:
            raise ValueError(f"Champ JSON manquant : {key}")

    if not isinstance(data["patches"], list):
        raise ValueError("'patches' doit être une liste.")

    return data
