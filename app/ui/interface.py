import sys
from pathlib import Path

# ---------------------------------------------------------------
# PATCH POUR STREAMLIT : ajoute la racine du projet au PYTHONPATH
# ---------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]   # remonte jusqu'à "Agent_smart_debeug-main"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# ---------------------------------------------------------------

import streamlit as st

from app.core.runner import run_script
from app.core.ai_client import query_ai
from app.core.validator import validate_json
from app.core.patcher import apply_patches


def find_python_in_venv(project_dir: Path):
    candidates = [".venv", "venv", "env"]

    for name in candidates:
        python_path = project_dir / name / "Scripts" / "python.exe"
        if python_path.exists():
            return python_path

    return None


def run_interface():
    st.title("🧠 IA Debugger – Interface Graphique")

    st.write("Sélectionnez un script Python à analyser et un environnement virtuel (venv).")

    base_dir = st.text_input(
        "Chemin du projet :", 
        value=str(Path.cwd())
    )

    base_path = Path(base_dir)

    if not base_path.exists():
        st.error("❌ Le dossier n’existe pas.")
        return

    py_files = list(base_path.glob("*.py"))

    if not py_files:
        st.warning("⚠ Aucun fichier .py trouvé dans ce dossier.")
        return

    script_file = st.selectbox("Choisir un fichier Python :", py_files)

    detected_python = find_python_in_venv(base_path)

    st.subheader("Environnement virtuel (venv)")
    if detected_python:
        st.success(f"Venv détecté automatiquement : {detected_python}")
    else:
        st.warning("⚠ Aucun venv détecté automatiquement.")

    python_bin = st.text_input(
        "Chemin du python.exe du venv :",
        value=str(detected_python) if detected_python else ""
    )

    if not python_bin:
        st.info("Veuillez entrer le chemin du venv ou en créer un dans ce dossier.")
        return

    if st.button("🚀 Lancer l'analyse IA"):
        st.info("Exécution du script…")

        code = script_file.read_text(encoding="utf-8")

        stdout, stderr = run_script(python_bin, str(script_file))

        st.subheader("📤 Sortie du script (stdout)")
        st.code(stdout, language="text")

        st.subheader("❌ Traceback (stderr)")
        st.code(stderr, language="python")

        if not stderr:
            st.success("Aucune erreur détectée dans le script.")
            return

        with st.spinner("Analyse IA en cours…"):
            raw_json = query_ai(code, stderr)

        st.subheader("📥 Réponse JSON IA brute")
        st.code(raw_json, language="json")

        try:
            data = validate_json(raw_json)
        except Exception as e:
            st.error(f"Erreur JSON : {e}")
            return

        st.subheader("🧠 Explication pédagogique")
        st.info(data["explanation"])

        st.subheader("🛠 Correctifs proposés")

        for p in data["patches"]:
            st.write(f"**Lignes {p['start_line']} → {p['end_line']} :**")
            st.code("\n".join(p["replacement"]), language="python")

        if st.button("✔ Appliquer les correctifs"):
            apply_patches(str(script_file), data["patches"])
            st.success("🎉 Correctifs appliqués avec succès !")


if __name__ == "__main__":
    run_interface()
