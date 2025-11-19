import sys
from pathlib import Path

from app.core.runner import run_script
from app.core.ai_client import query_ai
from app.core.validator import validate_json
from app.core.patcher import apply_patches

def find_python_in_venv(project_dir: Path):
    """
    Cherche automatiquement un venv dans le dossier du script.
    """
    candidates = [".venv", "venv", "env"]

    for name in candidates:
        python_path = project_dir / name / "Scripts" / "python.exe"
        if python_path.exists():
            return python_path

    return None


def main():
    if len(sys.argv) < 2:
        print("Usage : python iafix.py <chemin_du_script.py>")
        return

    script_path = Path(sys.argv[1]).resolve()

    if not script_path.exists():
        print(f"❌ Script introuvable : {script_path}")
        return

    project_dir = script_path.parent

    print(f"📁 Projet détecté : {project_dir}")

    python_bin = find_python_in_venv(project_dir)

    if python_bin is None:
        print("⚠ Aucun environnement virtuel trouvé dans le dossier.")
        python_bin = Path(input("Entrez le chemin vers python.exe du venv : ")).resolve()

    print(f"➡ Utilisation du venv : {python_bin}")

    code = script_path.read_text(encoding="utf-8")
    stdout, stderr = run_script(str(python_bin), str(script_path))

    print("\n=== STDOUT ===")
    print(stdout)

    print("\n=== TRACEBACK ===")
    print(stderr)

    if not stderr:
        print("✅ Aucun problème trouvé.")
        return

    print("\n🤖 Analyse IA...")
    raw_json = query_ai(code, stderr)
    data = validate_json(raw_json)

    print("\n📘 Explication pédagogique :")
    print(data["explanation"])

    if not data['fixable']:
        print("\n❌ Erreur non fixable :", data['reason'])
        return

    print("\n🛠 Correctifs proposés :")
    for p in data["patches"]:
        print(f"- Lignes {p['start_line']} → {p['end_line']}")
        for l in p["replacement"]:
            print("   ", l)

    choice = input("\n👉 Appliquer les correctifs ? (o/n) : ").strip().lower()
    if choice not in ["o", "oui", "y", "yes"]:
        print("❌ Correction annulée.")
        return

    apply_patches(script_path, data["patches"])
    print("\n🎉 Correctifs appliqués avec succès !")


if __name__ == "__main__":
    main()
