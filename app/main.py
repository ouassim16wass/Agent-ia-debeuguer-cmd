from pathlib import Path
from dotenv import load_dotenv

from app.core.config import load_config
from app.core.runner import run_script
from app.core.ai_client import query_ai
from app.core.validator import validate_json
from app.core.patcher import apply_patches

# Charge .env (clé Groq)
load_dotenv()

def main():
    cfg = load_config()

    project = Path(cfg["project_path"])
    venv = project / cfg["venv_name"] / "Scripts" / "python.exe"
    script = project / cfg["script_to_run"]

    print("🔍 Exécution du script...")
    stdout, stderr = run_script(str(venv), str(script))

    if stdout:
        print("\n=== STDOUT ===")
        print(stdout)

    print("\n=== TRACEBACK ===")
    print(stderr)

    if not stderr:
        print("\n✅ Aucune erreur détectée.")
        return

    code = script.read_text(encoding="utf-8")

    print("\n🤖 Appel du modèle IA...")
    raw_json = query_ai(code, stderr)

    print("\n=== JSON brut IA ===")
    print(raw_json)

    data = validate_json(raw_json)

    print("\n📘 Explication pédagogique :")
    print(data["explanation"])

    if not data["fixable"]:
        print("\n❌ Erreur non fixable automatiquement :")
        print(data["reason"])
        return

    print("\n🛠 Proposition de correctifs :")
    for patch in data["patches"]:
        print(f"- Lignes {patch['start_line']} à {patch['end_line']} seront remplacées par :")
        for line in patch["replacement"]:
            print(f"    {line}")

    # Confirmation utilisateur
    choice = input("\n👉 Voulez-vous appliquer les correctifs ? (o/n) : ").strip().lower()

    if choice not in ["o", "oui", "y", "yes"]:
        print("\n❎ Correction annulée.")
        return

    apply_patches(str(script), data["patches"])
    print("\n🎉 Correctifs appliqués avec succès !")

if __name__ == "__main__":
    main()
